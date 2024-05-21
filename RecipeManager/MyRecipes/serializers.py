from rest_framework import serializers
from MyRecipes.models import Recipe, Category, Ingredient, RecipeCategory, RecipeIngredient

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['recipe_id', 'title', 'description', 'preparation_time', 'instructions']
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id','name']
   

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['ingredient_id', 'name', 'quantity']
 
   
class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ['recipe', 'ingredient', 'quantity']
        
   
class RecipeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeCategory
        fields = ['recipe', 'category']
      
        

    