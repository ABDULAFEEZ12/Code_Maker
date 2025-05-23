from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    with open("static/index.html", "r") as file:
        return HTMLResponse(content=file.read(), status_code=200)

@app.get("/ai", response_class=HTMLResponse)
async def ai_assistant(request: Request):
    with open("static/ai.html", "r") as file:
        return HTMLResponse(content=file.read(), status_code=200)

@app.get("/ai-videos", response_class=HTMLResponse)
async def ai_videos(request: Request):
    with open("static/ai_videos.html", "r") as file:
        return HTMLResponse(content=file.read(), status_code=200)

@app.get("/success-roadmap", response_class=HTMLResponse)
async def success_roadmap(request: Request):
    with open("static/success_roadmap.html", "r") as file:
        return HTMLResponse(content=file.read(), status_code=200)
