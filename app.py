from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

def load_html(filename: str) -> str:
    filepath = os.path.join("templates", filename)
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return HTMLResponse(content=load_html("index.html"))

@app.get("/ai", response_class=HTMLResponse)
async def ai_assistant(request: Request):
    return HTMLResponse(content=load_html("ai.html"))

@app.get("/ai-videos-maker", response_class=HTMLResponse)
async def ai_videos_maker(request: Request):
    return HTMLResponse(content=load_html("ai_videos_maker.html"))

@app.get("/success-road-map", response_class=HTMLResponse)
async def success_road_map(request: Request):
    return HTMLResponse(content=load_html("success_road_map.html"))
