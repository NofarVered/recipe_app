from fastapi import APIRouter, HTTPException, status
import requests
from api_data_retrieve.recipe_processor_module import *


router = APIRouter()


@router.get("/search", status_code=200)
def get_players(search: str = "", dairy: str = "", gluten: str = ""):
    try:
        recipes = requests.get(
            f"https://recipes-goodness.herokuapp.com/recipes/{search}").json()["results"]
        filtered_recipes = filter_recipes(
            recipes, dairy, gluten)
        return {"recipes": filtered_recipes}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid searchInput"
        )
