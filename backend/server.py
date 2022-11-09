from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from create_db_script.load_data import load
from routers import recipes_router

app = FastAPI()

# load()

app.include_router(recipes_router.router)


@app.get("/sanity")
def root():
    return {"message": "Server is running"}


app.mount("/", StaticFiles(directory="./client/build", html=True), name="client")

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
