from django.contrib import admin
from .models import Recipe, Ingredient, Category, RecipeIngredient, RecipeCategory

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'preparation_time', 'instructions']

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'ingredient', 'quantity']

class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'category']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeCategory, RecipeCategoryAdmin)
