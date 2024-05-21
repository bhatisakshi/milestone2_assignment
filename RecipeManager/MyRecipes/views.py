from .models import Recipe, Ingredient, Category, RecipeIngredient, RecipeCategory
from rest_framework import generics
from django.shortcuts import render, redirect, get_object_or_404 
from .serializers import RecipeSerializer, IngredientSerializer, CategorySerializer, RecipeCategorySerializer, RecipeIngredientSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection



class RecipeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
class RecipeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class IngredientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    
class IngredientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
      
class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class RecipeCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeCategorySerializer
    
      
class RecipeCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeCategorySerializer
    
class RecipeIngredientListCreateAPIView(generics.ListCreateAPIView):
    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeIngredientSerializer
      
class RecipeIngredientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeIngredientSerializer
    


@api_view(['GET'])
def get_recipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_ingredients(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_recipecategories(request):
    recipecategories = RecipeCategory.objects.all()
    serializer = RecipeCategorySerializer(recipecategories, many=True)
    return Response(serializer.data)
  
    
@api_view(['GET'])
def get_recipeingredients(request):
    recipeingredients = RecipeIngredient.objects.all()
    serializer = RecipeIngredientSerializer(recipeingredients, many=True)
    return Response(serializer.data)


def home(request):
    return render(request, 'home.html')



