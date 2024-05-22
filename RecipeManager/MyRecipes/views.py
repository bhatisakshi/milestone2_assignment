from .models import Recipe, Ingredient, Category, RecipeIngredient, RecipeCategory
from rest_framework import generics
from django.shortcuts import render
from .serializers import RecipeSerializer, IngredientSerializer, CategorySerializer, RecipeCategorySerializer, RecipeIngredientSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class RecipeListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of recipes or create a new recipe.
    
    - GET: Returns a list of all recipes.
    - POST: Creates a new recipe.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
class RecipeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a recipe.
    
    - GET: Retrieves a recipe by ID.
    - PUT: Updates a recipe by ID.
    - DELETE: Deletes a recipe by ID.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class IngredientListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of ingredients or create a new ingredient.
    
    - GET: Returns a list of all ingredients.
    - POST: Creates a new ingredient.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    
class IngredientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete an ingredient.
    
    - GET: Retrieves an ingredient by ID.
    - PUT: Updates an ingredient by ID.
    - DELETE: Deletes an ingredient by ID.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of categories or create a new category.
    
    - GET: Returns a list of all categories.
    - POST: Creates a new category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
      
class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a category.
    
    - GET: Retrieves a category by ID.
    - PUT: Updates a category by ID.
    - DELETE: Deletes a category by ID.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class RecipeCategoryListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of recipe categories or create a new recipe category.
    
    - GET: Returns a list of all recipe categories.
    - POST: Creates a new recipe category.
    """
    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeCategorySerializer
      
class RecipeCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a recipe category.
    
    - GET: Retrieves a recipe category by ID.
    - PUT: Updates a recipe category by ID.
    - DELETE: Deletes a recipe category by ID.
    """
    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeCategorySerializer
    
class RecipeIngredientListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of recipe ingredients or create a new recipe ingredient.
    
    - GET: Returns a list of all recipe ingredients.
    - POST: Creates a new recipe ingredient.
    """
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer
      
class RecipeIngredientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a recipe ingredient.
    
    - GET: Retrieves a recipe ingredient by ID.
    - PUT: Updates a recipe ingredient by ID.
    - DELETE: Deletes a recipe ingredient by ID.
    """
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer

@api_view(['GET'])
def get_recipes(request):
    """
    API view to retrieve a list of all recipes.
    
    - GET: Returns a list of all recipes.
    """
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_ingredients(request):
    """
    API view to retrieve a list of all ingredients.
    
    - GET: Returns a list of all ingredients.
    """
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_categories(request):
    """
    API view to retrieve a list of all categories.
    
    - GET: Returns a list of all categories.
    """
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_recipecategories(request):
    """
    API view to retrieve a list of all recipe categories.
    
    - GET: Returns a list of all recipe categories.
    """
    recipecategories = RecipeCategory.objects.all()
    serializer = RecipeCategorySerializer(recipecategories, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def get_recipeingredients(request):
    """
    API view to retrieve a list of all recipe ingredients.
    
    - GET: Returns a list of all recipe ingredients.
    """
    recipeingredients = RecipeIngredient.objects.all()
    serializer = RecipeIngredientSerializer(recipeingredients, many=True)
    return Response(serializer.data)

def home(request):
    """
    View to render the home page.
    
    - GET: Renders the home page template.
    """
    return render(request, 'home.html')
