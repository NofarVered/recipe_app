from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi import HTTPException, status
import requests
from create_db_script.load_data import load
from api_data_retrieve import recipe_processor_model
app = FastAPI()

load()


@app.get("/sanity")
def root():
    return {"message": "Server is running"}


@app.get("/search", status_code=200)
async def get_players(search: str = "", dairy: str = "", gluten: str = ""):
    try:
        recipes = requests.get(
            f"https://recipes-goodness.herokuapp.com/recipes/{search}").json()["results"]
        filtered_recipes = recipe_processor_model.filter_recipes(
            recipes, dairy, gluten)
        # print(filtered_recipes)
        return {"recipes": filtered_recipes}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid searchInput"
        )

app.mount("/", StaticFiles(directory="../client/build", html=True), name="client")

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
