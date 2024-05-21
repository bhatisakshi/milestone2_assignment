from django.db import models
from django.db import connection

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    preparation_time = models.IntegerField()
    instructions = models.TextField()

    def __str__(self):
        return self.title
    


class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='Uncategorized')

    def __str__(self):
        return self.name, self.category_id



class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=20)

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




