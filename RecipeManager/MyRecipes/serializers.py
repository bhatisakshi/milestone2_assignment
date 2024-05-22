from rest_framework import serializers
from MyRecipes.models import Recipe, Category, Ingredient, RecipeCategory, RecipeIngredient

class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Recipe model.
    
    Serializes all fields of the Recipe model including:
    - recipe_id: ID of the recipe.
    - title: Title of the recipe.
    - description: Description of the recipe.
    - preparation_time: Time required to prepare the recipe in minutes.
    - instructions: Step-by-step instructions for preparing the recipe.
    """
    class Meta:
        model = Recipe
        fields = ['recipe_id', 'title', 'description', 'preparation_time', 'instructions']
    

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    
    Serializes all fields of the Category model including:
    - category_id: ID of the category.
    - name: Name of the category.
    """
    class Meta:
        model = Category
        fields = ['category_id', 'name']
   

class IngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Ingredient model.
    
    Serializes all fields of the Ingredient model including:
    - ingredient_id: ID of the ingredient.
    - name: Name of the ingredient.
    - quantity: Default quantity of the ingredient.
    """
    class Meta:
        model = Ingredient
        fields = ['ingredient_id', 'name', 'quantity']
 
   
class RecipeIngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for the RecipeIngredient model.
    
    Serializes all fields of the RecipeIngredient model including:
    - recipe: Reference to the related recipe.
    - ingredient: Reference to the related ingredient.
    - quantity: Quantity of the ingredient used in the recipe.
    """
    class Meta:
        model = RecipeIngredient
        fields = ['recipe', 'ingredient', 'quantity']
        
   
class RecipeCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the RecipeCategory model.
    
    Serializes all fields of the RecipeCategory model including:
    - recipe: Reference to the related recipe.
    - category: Reference to the related category.
    """
    class Meta:
        model = RecipeCategory
        fields = ['recipe', 'category']
