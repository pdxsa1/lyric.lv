from app.routes import lyrics,songs
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(songs.router)
@app.get("/")
def root():
    return {"message": "Welcome to lyric.lv backend"}

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "..", "static")),
    name="static"
)
