from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# Allow frontend access (e.g., GitHub Pages or local dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace * with specific frontend URL if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route for testing
@app.get("/")
def home():
    return {"message": "Code Maker API is running 🔥"}

# OpenRouter chat completion API
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.post("/generate")
async def generate_code(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",  # You can change this to another model on OpenRouter
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        completion = response.json()["choices"][0]["message"]["content"]
        return {"result": completion}
    else:
        return {"error": response.text}
