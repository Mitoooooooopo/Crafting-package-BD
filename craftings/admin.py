from typing import TYPE_CHECKING, Any

from django.contrib import admin
from .models import CraftingRecipe, CraftingIngredient
from django.utils.safestring import mark_safe

class CraftingIngredientInline(admin.TabularInline):
    model = CraftingIngredient
    extra = 1
    autocomplete_fields = ("ingredient",)
    fields = ("ingredient", "quantity") 
    
@admin.register(CraftingRecipe)
class CraftingRecipeAdmin(admin.ModelAdmin):
    list_display = ("result",)
    inlines = [CraftingIngredientInline]
    search_fields = ("result__name",)
    autocomplete_fields = ("result",) 
    
