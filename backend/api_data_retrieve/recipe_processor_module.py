from .db_manager import db_manager
from .recipe import Recipe


def _is_recipe_dairy_free(recipe: Recipe):
    dairy_ingrediants = db_manager.get_dairy()
    for ingrediant in recipe.ingredients:
        if ingrediant in dairy_ingrediants:
            return False
    return True


def _is_recipe_gluten_free(recipe: Recipe):
    gluten_ingrdiants = db_manager.get_gluten()
    for ingrediant in recipe.ingredients:
        if ingrediant in gluten_ingrdiants:
            return False
    return True


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
