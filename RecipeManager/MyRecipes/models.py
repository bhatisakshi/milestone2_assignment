from django.db import models

class Recipe(models.Model):
    """
    Represents a recipe in the system.
    
    Attributes:
        recipe_id (int): Primary key for the recipe.
        title (str): Title of the recipe.
        description (str): Description of the recipe.
        preparation_time (int): Time required to prepare the recipe in minutes.
        instructions (str): Step-by-step instructions for preparing the recipe.
    """
    recipe_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    preparation_time = models.IntegerField()
    instructions = models.TextField()

    class Meta:
        verbose_name_plural = "Recipes"   # Plural form

    def __str__(self):
        """
        Returns the string representation of the recipe, which is its title.
        """
        return self.title


class Ingredient(models.Model):
    """
    Represents an ingredient used in recipes.
    
    Attributes:
        ingredient_id (int): Primary key for the ingredient.
        name (str): Name of the ingredient.
        quantity (str): Default quantity of the ingredient.
    """
    ingredient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Ingredients"   # Plural form

    def __str__(self):
        """
        Returns the string representation of the ingredient, which is its name.
        """
        return self.name


class Category(models.Model):
    """
    Represents a category for recipes.
    
    Attributes:
        category_id (int): Primary key for the category.
        name (str): Name of the category.
    """
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"   # Plural form

    def __str__(self):
        """
        Returns the string representation of the category, which is its name and ID.
        """
        return self.name


class RecipeIngredient(models.Model):
    """
    Represents the relationship between recipes and ingredients.
    
    Attributes:
        recipe (Recipe): The recipe that uses the ingredient.
        ingredient (Ingredient): The ingredient used in the recipe.
        quantity (str): The quantity of the ingredient used in the recipe.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "RecipeIngredients"   # Plural form

    def __str__(self):
        """
        Returns the string representation of the category, which is its name and ID.
        """
        return f"{self.recipe.title} - {self.ingredient.name}" 
    

class RecipeCategory(models.Model):
    """
    Represents the relationship between recipes and categories.
    
    Attributes:
        recipe (Recipe): The recipe categorized.
        category (Category): The category to which the recipe belongs.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "RecipeCategories"   # Plural form

    def __str__(self):
        """
        Returns the string representation of the category, which is its name and ID.
        """
        return f"{self.recipe.title} - {self.category.name}" 