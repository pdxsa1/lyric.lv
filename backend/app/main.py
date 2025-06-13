from app.routes import lyrics,songs
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to lyric.lv backend"}

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "..", "static")),
    name="static"
)
