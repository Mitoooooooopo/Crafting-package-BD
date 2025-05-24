from discord.ui import Button, View
from discord.ext import commands
from discord import app_commands
from typing import TYPE_CHECKING
import discord
import random

from .models import CraftingRecipe
from .models import CraftingIngredient
from ballsdex.settings import settings
from .transformers import CraftTransform
from ballsdex.core.utils.transformers import BallEnabledTransform
from ballsdex.core.utils.transformers import SpecialEnabledTransform
from ballsdex.core.bot import BallsDexBot

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot

from ballsdex.core.models import (
    Ball,
    BallInstance,
    BlacklistedGuild,
    BlacklistedID,
    GuildConfig,
    Player,
    Trade,
    TradeObject,
    balls,
    specials,
)

class craft(commands.GroupCog):
    """
    Crafting commands.
    """

    def __init__(self, bot: "BallsDexBot"):
        self.bot = bot

    @app_commands.command()
    async def countryball(
        self,
        interaction: discord.Interaction,
        countryball: CraftTransform,
        an_special: SpecialEnabledTransform = None,
    ):
        """
        craft a countryball.

        Parameters
        ----------
        countryball: CraftTransform
           countryball you want to craft
        """
        recipe = countryball

        player, _ = await Player.get_or_create(discord_id=interaction.user.id)

        # Grab all ball type IDs the player owns
        player_owned_ball_type_ids = await BallInstance.filter(player=player).values_list("ball_id", flat=True)
        player_owned_ball_type_ids = list(player_owned_ball_type_ids)

        ingredients = await recipe.ingredients.all().prefetch_related("ingredient")

        for ingredient in ingredients:
            ball_id = ingredient.ingredient_id
            # do your logic with ball_id and ingredient.quantity

        used_instances = []
        missing = []

        for ingredient in ingredients:
            ball_id = ingredient.ingredient_id
            quantity = ingredient.quantity

            # Check if player owns this ball type
            if ball_id not in player_owned_ball_type_ids:
                emoji = self.bot.get_emoji(ingredient.ingredient.emoji_id)
                missing.append((ingredient.ingredient.country, emoji, quantity))
                continue

            # Check if player owns the required ball type (with correct special if needed)
            filter_conditions = {"player": player, "ball_id": ball_id}
            if an_special is not None:
                filter_conditions["special"] = an_special
            else:
                filter_conditions["special"] = None

            owned_instances = await BallInstance.filter(**filter_conditions).limit(quantity).all()

            if len(owned_instances) < quantity:
                emoji = self.bot.get_emoji(ingredient.ingredient.emoji_id)
                special_prefix = f"{an_special.emoji} {an_special.name} " if an_special else ""
                missing.append((f"{special_prefix}{ingredient.ingredient.country}", emoji, quantity - len(owned_instances)))
            else:
                used_instances.extend(owned_instances)

        # Handle missing balls
        if missing:
            missing_msg = "\n".join(f"- {emoji} {name} x{qty}" for name, emoji, qty in missing)
            await interaction.response.send_message(
                f"❌ You're missing the following {settings.plural_collectible_name} to craft:\n{missing_msg}", ephemeral=True
            )
            return

        await recipe.fetch_related("result")
        crafted_instance = await BallInstance.create(
            player=player,
            ball=recipe.result,
            special=an_special if an_special else None,
            health_bonus=random.randint(-settings.max_attack_bonus, settings.max_attack_bonus),
            attack_bonus=random.randint(-settings.max_attack_bonus, settings.max_attack_bonus),
        )

        name = f" {an_special.emoji} {an_special.name} {recipe.result.country}" if an_special else recipe.result.country

        await interaction.response.send_message(
            f"✅ Wow successfully crafted **{name}**!", ephemeral=True
        )

        await BallInstance.filter(id__in=[ball.id for ball in used_instances]).delete()
