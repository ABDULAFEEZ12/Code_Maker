from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (e.g. CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Helper function to load HTML
def load_html(filename: str) -> str:
    filepath = os.path.join("templates", filename)
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return HTMLResponse(content=load_html("index.html"))

@app.get("/ai", response_class=HTMLResponse)
async def ai_assistant(request: Request):
    return HTMLResponse(content=load_html("ai.html"))

@app.get("/code-playground", response_class=HTMLResponse)
async def code_playground(request: Request):
    return HTMLResponse(content=load_html("code_playground.html"))
