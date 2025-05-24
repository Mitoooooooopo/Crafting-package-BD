import logging
import time
from datetime import timedelta
from enum import Enum
from typing import TYPE_CHECKING, Generic, Iterable, Optional, TypeVar

import discord
from discord import app_commands
from discord.interactions import Interaction
from tortoise.exceptions import DoesNotExist
from tortoise.expressions import Q, RawSQL
from tortoise.models import Model
from tortoise.timezone import now as tortoise_now
from ballsdex.core.bot import BallsDexBot 
from ballsdex.core.utils.transformers import ModelTransformer, ValidationError
from .models import CraftingRecipe
from ballsdex.core.models import (
    Ball,
    BallInstance,
)  

class CraftTransformer(ModelTransformer[CraftingRecipe]):
    name = "craft"
    model = CraftingRecipe()

    def key(self, model: CraftingRecipe) -> str:
        return f"Recipe #{model.pk}"

    async def load_items(self) -> Iterable[CraftingRecipe]:
        return await CraftingRecipe.all().prefetch_related("result")

    async def get_options(
        self, interaction: discord.Interaction["BallsDexBot"], value: str
    ) -> list[app_commands.Choice[str]]:
        items = await self.load_items()
        return [
            app_commands.Choice(
                name=f"{item.result.country}", value=f"{item.pk}"
            )
            for item in items
            if value.lower() in item.result.country.lower()
        ][:25]

    async def transform(
        self, interaction: discord.Interaction["BallsDexBot"], value: str
    ) -> Optional[CraftingRecipe]:
        try:
            items = await self.load_items()
            for recipe in items:
                if str(recipe.pk) == value:
                    return recipe
            raise ValueError
        except ValueError:
            await interaction.response.send_message(
                "That recipe doesn't exist. Please use the autocomplete to pick one.",
                ephemeral=True,
            )
            return None
            
CraftTransform = app_commands.Transform[CraftingRecipe, CraftTransformer] 
