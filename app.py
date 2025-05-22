from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import requests
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home route with TELAVISTA branding
@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>TELAVISTA</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f9f9f9; }
            h1 { color: #2b7a78; }
            textarea { width: 100%; height: 150px; }
            button { padding: 10px 20px; margin-top: 10px; background-color: #2b7a78; color: white; border: none; cursor: pointer; }
            button:hover { background-color: #205d5a; }
            pre { background-color: #f4f4f4; padding: 10px; white-space: pre-wrap; border: 1px solid #ccc; }
        </style>
    </head>
    <body>
        <h1>🌍 TELAVISTA</h1>
        <p>Your AI-powered education & coding assistant.</p>
        <textarea id="prompt" placeholder="e.g. Explain binary trees or Write a Python function..."></textarea><br/>
        <button onclick="generateCode()">Generate</button>
        <h3>Response:</h3>
        <pre id="result"></pre>

        <script>
            async function generateCode() {
                const prompt = document.getElementById('prompt').value;
                if (!prompt) {
                    alert("Please enter a prompt.");
                    return;
                }
                const response = await fetch('/generate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ prompt })
                });
                const data = await response.json();
                if (data.result) {
                    document.getElementById('result').textContent = data.result;
                } else if (data.error) {
                    document.getElementById('result').textContent = "Error: " + data.error;
                }
            }
        </script>
    </body>
    </html>
    """
    return html_content

# OpenRouter API handler
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.post("/generate")
async def generate_code(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return {"error": "OPENROUTER_API_KEY is not set in environment."}

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",  # or gpt-4 etc.
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            completion = response.json()["choices"][0]["message"]["content"]
            return {"result": completion}
        else:
            return {"error": response.text}
    except Exception as e:
        return {"error": str(e)}
