# Create a list of numbers
import csv  # Imports a package to read the code


class Recipe:
    def __init__(self, name, ingredients,
                 instructions):  # Self represents the instance of the class recipe. It allows access and manipulate
        # the attributes and methods of the instance within the class.
        self.name = name
        self.ingredients = ingredients  # Store ingredients as a set
        self.instructions = instructions


class RecipeBook:
    def __init__(self):
        self.recipes = {}  # Use a dictionary to store recipes (name -> Recipe object)

    def add_recipe(self, recipe):
        self.recipes[recipe.name] = recipe

    def find_recipes_with_ingredient(self, ingredient):
        return [recipe for recipe in self.recipes.values() if
                ingredient in recipe.ingredients]  # Returns a LIST of recipes containing the ingredients

    # Add methods to view, update, and delete recipes.
    def update_recipe_instructions(self, recipe_name, new_instructions):
        if recipe_name in self.recipes:
            self.recipes[recipe_name].instructions = new_instructions
            print(f"Instructions for {recipe_name} have been updated to '{new_instructions}'.")
        else:
            print(f"No recipe found with the name {recipe_name}.")

    def delete_recipe(self, recipe_name):
        if recipe_name in self.recipes:
            del self.recipes[recipe_name]
            print(f"{recipe_name} has been deleted from the recipe book.")
        else:
            print(f"No recipe found with the name {recipe_name}.")


# Function to read recipes from a CSV file
def read_recipes_from_csv(file_path):
    recipe_book = RecipeBook()

    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)  # Allows you to read the csv in rows and columns as items
        for row in reader:
            name = row['Name'].lower()
            # Split ingredients by comma and store as a set
            ingredients = set(row['Ingredients'].lower().split('+'))  # store ingredients as sets
            instructions = row.get('Instructions', '')
            recipe = Recipe(name, ingredients, instructions)
            recipe_book.add_recipe(recipe)

    return recipe_book


# Sample usage: Read recipes from a CSV file
csv_file_path = 'recipe.csv'  # Update with your CSV file path
recipe_book = read_recipes_from_csv(csv_file_path)


def main():
    # User input to find recipes with a specific ingredient
    search_ingredient = input("Enter an ingredient to find recipes: ")
    found_recipes = recipe_book.find_recipes_with_ingredient(search_ingredient.lower())

    if found_recipes:
        print(f"Recipes that include {search_ingredient}:")
        for recipe in found_recipes:
            print(f"Recipe: {recipe.name}")
            print("Ingredients:")
            for ingredient in recipe.ingredients:
                print(f"  {ingredient}")
            print("Instructions:")
            print(recipe.instructions)
            print()
    else:
        print(f"No recipes found with {search_ingredient}.")

    # Access recipes by name
    recipe_name = input("Enter a recipe name to view details: ")
    if recipe_name.lower() in recipe_book.recipes:
        selected_recipe = recipe_book.recipes[recipe_name]  # Selection Statement
        print(f"Recipe: {selected_recipe.name}")
        print("Ingredients:")
        for ingredient in selected_recipe.ingredients:
            print(f"  {ingredient}")
        print("Instructions:")
        print(selected_recipe.instructions)
        print()
        manage(selected_recipe, recipe_book)
    else:
        print(f"No recipe found with the name {recipe_name}.")


def manage(selected_recipe, recipe_book):
    while True:  # Allows user to try multiple times
        manage_recipe = input("Do you want to update or delete the recipe? Enter 'Update' or 'Delete' (or press the "
                              "'Enter' key to start over): ")

        if manage_recipe.lower() == "update":
            new_instructions = input("Enter the new instructions: ")
            recipe_book.update_recipe_instructions(selected_recipe.name, new_instructions)
            break  # Exit the loop

        elif manage_recipe.lower() == "delete":
            recipe_book.delete_recipe(selected_recipe.name)
            break  # Exit the loop

        elif not manage_recipe:  # User pressed 'Enter'
            break  # Exit the loop

        else:
            print("Invalid input. Please enter 'Update' to update the recipe, 'Delete' to delete, or press 'Enter' to "
                  "start over.")


if __name__ == '__main__':
    # Call the main function to start the program
    main()
