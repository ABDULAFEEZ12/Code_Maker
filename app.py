import os
import openai
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Set OpenAI API key from environment variable
OPENAI_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("Please set the OPENROUTER_API_KEY environment variable.")
openai.api_key = OPENAI_API_KEY

# Enable CORS for all origins (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str
    section: Optional[str] = ""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTMLResponse("""<!DOCTYPE html><html><head><title>Telavista</title></head><body><h1>Welcome to Telavista</h1></body></html>""")

@app.post("/ask")
async def ask(request: AskRequest):
    question = request.question
    section = request.section

    prompt = f"Section: {section}\nQuestion: {question}\nAnswer:"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            n=1,
            stop=["\n"]
        )
        answer = response.choices[0].text.strip()
    except Exception as e:
        print(f"OpenAI API call failed: {e}")
        answer = "Sorry, I couldn't generate a response at the moment."

    return JSONResponse({"answer": answer})

# Additional educational tools endpoints
@app.post("/summarize")
async def summarize_text(request: Request):
    data = await request.json()
    text = data.get("text", "")

    prompt = f"Summarize this text in a few sentences:\n{text}"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            temperature=0.5,
            n=1
        )
        summary = response.choices[0].text.strip()
    except Exception as e:
        print(f"Error summarizing: {e}")
        summary = "Sorry, I couldn't generate a summary."

    return JSONResponse({"summary": summary})

@app.post("/motivate")
async def generate_motivation(request: Request):
    data = await request.json()
    topic = data.get("topic", "your goals")

    prompt = f"Give a motivational message about {topic}:"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            temperature=0.8,
            n=1
        )
        message = response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating motivation: {e}")
        message = "Stay strong! You're capable of amazing things."

    return JSONResponse({"message": message})

@app.post("/studyplan")
async def create_study_plan(request: Request):
    data = await request.json()
    subject = data.get("subject", "Mathematics")
    weeks = data.get("weeks", 4)

    prompt = f"Create a {weeks}-week study plan for {subject}."

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7,
            n=1
        )
        plan = response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating study plan: {e}")
        plan = "Couldn't generate a study plan. Try again later."

    return JSONResponse({"plan": plan})

@app.post("/goalmap")
async def generate_goal_map(request: Request):
    data = await request.json()
    goal = data.get("goal", "become a top student")

    prompt = f"Break down the steps to achieve this goal: {goal}"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.6,
            n=1
        )
        steps = response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating goal steps: {e}")
        steps = "Sorry, couldn't create a roadmap at the moment."

    return JSONResponse({"steps": steps})

@app.get("/status")
async def status():
    return {"status": "Telavista backend is running smoothly."}
