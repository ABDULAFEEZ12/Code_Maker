from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# Allow frontend (e.g., from GitHub Pages)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify only your frontend URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenRouter endpoint
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
        "model": "openai/gpt-3.5-turbo",  # Or use another model from OpenRouter
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        completion = response.json()["choices"][0]["message"]["content"]
        return {"result": completion}
    else:
        return {"error": response.text}
