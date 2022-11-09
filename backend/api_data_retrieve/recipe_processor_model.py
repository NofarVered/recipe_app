from .db_manager import db_manager
from .recipe import Recipe


def _is_recipe_dairy_free(recipe: Recipe):
    recipe_ingrediants = recipe.ingredients
    dairy_ingrediants = db_manager.get_dairy()
    result = any(
        map(lambda ingrediant: ingrediant in dairy_ingrediants, recipe_ingrediants))
    return result != True


def _is_recipe_gluten_free(recipe: Recipe):
    recipe_ingrediants = recipe.ingredients
    gluten_ingrdiants = db_manager.get_gluten()
    result = any(
        map(lambda ingrediant: ingrediant in gluten_ingrdiants, recipe_ingrediants))
    return result != True


def filter_recipes(recipes, dairyFree, glutenFree):
    recipesData = []
    dairyFree = True if dairyFree == "true" else False
    glutenFree = True if glutenFree == "true" else False
    for recipe in recipes:
        recipesData.append(Recipe(**recipe))
    if dairyFree:
        recipesData = [
            recipe for recipe in recipesData if _is_recipe_dairy_free(recipe)]
    if glutenFree:
        recipesData = [
            recipe for recipe in recipesData if _is_recipe_gluten_free(recipe)]
    return list(recipesData)
