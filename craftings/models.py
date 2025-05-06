from __future__ import annotations

from datetime import timedelta
from typing import Any, Iterable, cast

from django.contrib import admin
from django.core.cache import cache
from django.db import models
from django.utils.safestring import SafeText, mark_safe
from django.utils.timezone import now
from bd_models.models import Ball, Player 
from ballsdex.settings import settings 

class CraftingRecipe(models.Model):
    result = models.ForeignKey(Ball, on_delete=models.CASCADE, related_name="crafted_by") 
    
    class Meta:
        managed = True
        db_table = "craftingrecipe"

    def __str__(self):
        if self.result:
            return f"{self.result} Recipe"
        return "Unnamed Crafting Recipe"


class CraftingIngredient(models.Model):
    recipe = models.ForeignKey("CraftingRecipe", on_delete=models.CASCADE, related_name="ingredients")
    ingredient = models.ForeignKey(Ball, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        managed = True
        db_table = "craftingingredient" 
        unique_together = ("recipe", "ingredient") 
        
    def __str__(self):
        if self.recipe:
            return f"{self.recipe} Recipe"
        return "Unnamed Crafting Recipe"
