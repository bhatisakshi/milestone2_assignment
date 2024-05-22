from django.contrib import admin
from django.urls import path
from MyRecipes.views import( RecipeListCreateAPIView, 
                            RecipeRetrieveUpdateDestroyAPIView, 
                            IngredientListCreateAPIView, 
                            IngredientRetrieveUpdateDestroyAPIView, 
                            CategoryListCreateAPIView, 
                            CategoryRetrieveUpdateDestroyAPIView, 
                            RecipeCategoryListCreateAPIView, 
                            RecipeCategoryRetrieveUpdateDestroyAPIView, 
                            RecipeIngredientListCreateAPIView, 
                            RecipeIngredientRetrieveUpdateDestroyAPIView,
                            home,
                            get_recipes,
                            get_ingredients,
                            get_categories,
                            get_recipecategories,
                            get_recipeingredients,
)

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', RecipeListCreateAPIView.as_view(), name='recipe-home'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDestroyAPIView.as_view(), name='recipe-detail'),
    path('get-recipes/', get_recipes, name='get_recipes' ),
    
    path('ingredients/', IngredientListCreateAPIView.as_view(), name='ingredient-list-create'),
    path('ingredients/<int:pk>/', IngredientRetrieveUpdateDestroyAPIView.as_view(), name='ingredient-detail'),
    path('get-ingredients/', get_ingredients, name='get_ingredients' ),
    
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('get-categories/', get_categories, name='get_categories' ),
    
    path('recipeingredients/', RecipeIngredientListCreateAPIView.as_view(), name='recipeingredient-list-create'),
    path('recipeingredients/<int:pk>/', RecipeIngredientRetrieveUpdateDestroyAPIView.as_view(), name='recipeingredient-detail'),
    path('get-recipecategories/', get_recipecategories, name='get_recipecategories' ),
    
    path('recipecategories/', RecipeCategoryListCreateAPIView.as_view(), name='recipecategories--list-create'),
    path('recipecategories/<int:pk>/', RecipeCategoryRetrieveUpdateDestroyAPIView.as_view(), name='recipecategory-detail'),
    path('get-recipeingredients/', get_recipeingredients, name='get_recipeingredients' ),
    
    path('admin/', admin.site.urls),
]

