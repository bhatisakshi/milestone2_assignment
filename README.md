# MyRecipes API

MyRecipes is a Django-based API for managing recipes, ingredients, and categories. It allows users to create, retrieve, update, and delete recipes, ingredients, and their relationships.

## Features

- Create, retrieve, update, and delete recipes
- Create, retrieve, update, and delete ingredients
- Create, retrieve, update, and delete categories
- Manage relationships between recipes and ingredients
- Manage relationships between recipes and categories
- Home page for the application

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/MyRecipes.git
    ```

2. Navigate to the project directory:
    ```sh
    cd MyRecipes
    ```

3. Create and activate a virtual environment:
    ```sh
    virtualenv virenv
    source virenv/bin/activate  
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser for accessing the admin interface:
    ```sh
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```sh
    python manage.py runserver
    ```

## API Endpoints

### Home Page

- `GET /`
    - Renders the home page.

### Recipes

- `GET /recipes/`
    - Retrieves a list of all recipes.
- `POST /recipes/`
    - Creates a new recipe.
- `GET /recipes/<int:pk>/`
    - Retrieves a specific recipe by ID.
- `PUT /recipes/<int:pk>/`
    - Updates a specific recipe by ID.
- `DELETE /recipes/<int:pk>/`
    - Deletes a specific recipe by ID.
- `GET /get-recipes/`
    - Retrieves a list of all recipes.

### Ingredients

- `GET /ingredients/`
    - Retrieves a list of all ingredients.
- `POST /ingredients/`
    - Creates a new ingredient.
- `GET /ingredients/<int:pk>/`
    - Retrieves a specific ingredient by ID.
- `PUT /ingredients/<int:pk>/`
    - Updates a specific ingredient by ID.
- `DELETE /ingredients/<int:pk>/`
    - Deletes a specific ingredient by ID.
- `GET /get-ingredients/`
    - Retrieves a list of all ingredients.

### Categories

- `GET /categories/`
    - Retrieves a list of all categories.
- `POST /categories/`
    - Creates a new category.
- `GET /categories/<int:pk>/`
    - Retrieves a specific category by ID.
- `PUT /categories/<int:pk>/`
    - Updates a specific category by ID.
- `DELETE /categories/<int:pk>/`
    - Deletes a specific category by ID.
- `GET /get-categories/`
    - Retrieves a list of all categories.

### Recipe-Ingredient Relationships

- `GET /recipeingredients/`
    - Retrieves a list of all recipe-ingredient relationships.
- `POST /recipeingredients/`
    - Creates a new recipe-ingredient relationship.
- `GET /recipeingredients/<int:pk>/`
    - Retrieves a specific recipe-ingredient relationship by ID.
- `PUT /recipeingredients/<int:pk>/`
    - Updates a specific recipe-ingredient relationship by ID.
- `DELETE /recipeingredients/<int:pk>/`
    - Deletes a specific recipe-ingredient relationship by ID.
- `GET /get-recipeingredients/`
    - Retrieves a list of all recipe-ingredient relationships.

### Recipe-Category Relationships

- `GET /recipecategories/`
    - Retrieves a list of all recipe-category relationships.
- `POST /recipecategories/`
    - Creates a new recipe-category relationship.
- `GET /recipecategories/<int:pk>/`
    - Retrieves a specific recipe-category relationship by ID.
- `PUT /recipecategories/<int:pk>/`
    - Updates a specific recipe-category relationship by ID.
- `DELETE /recipecategories/<int:pk>/`
    - Deletes a specific recipe-category relationship by ID.
- `GET /get-recipecategories/`
    - Retrieves a list of all recipe-category relationships.

## Models

### Recipe

- `recipe_id`: ID of the recipe.
- `title`: Title of the recipe.
- `description`: Description of the recipe.
- `preparation_time`: Time required to prepare the recipe in minutes.
- `instructions`: Step-by-step instructions for preparing the recipe.

### Ingredient

- `ingredient_id`: ID of the ingredient.
- `name`: Name of the ingredient.
- `quantity`: Default quantity of the ingredient.

### Category

- `category_id`: ID of the category.
- `name`: Name of the category.

### RecipeIngredient

- `recipe`: Reference to the related recipe.
- `ingredient`: Reference to the related ingredient.
- `quantity`: Quantity of the ingredient used in the recipe.

### RecipeCategory

- `recipe`: Reference to the related recipe.
- `category`: Reference to the related category.

## Admin Interface

To access the Django admin interface, go to `/admin/` and log in with the superuser credentials created during the installation process.
