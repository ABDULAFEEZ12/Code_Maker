import os
import openai
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Load DeepAI API key from environment
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

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Telavista - Your Personal Learning Companion</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />

<!-- Styles -->
<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    background-color: #f0f4f8;
    color: #333;
  }
  header {
    background-color: #2b7a78;
    color: white;
    padding: 40px 20px;
    text-align: center;
  }
  header h1 {
    font-size: 3em;
    margin: 0 0 10px 0;
  }
  header p {
    font-size: 1.2em;
    margin: 0;
  }
  .tab {
    display: flex;
    justify-content: center;
    background-color: #333;
    overflow: hidden;
  }
  .tab button {
    background-color: inherit;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    transition: 0.3s;
    font-size: 17px;
    color: white;
  }
  .tab button:hover {
    background-color: #ddd;
    color: black;
  }
  .tab button.active {
    background-color: #2b7a78;
    color: white;
  }
  .section {
    display: none;
    padding: 20px;
    background-color: #fff;
    margin: 20px auto;
    max-width: 1000px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
  /* Chat styles */
  #messages {
    max-height: 300px;
    overflow-y: auto;
    border: 1px solid #ccc;
    padding: 10px;
    margin-top: 10px;
  }
  .user-message {
    text-align: right;
    background-color: #e1f5fe;
    padding: 8px;
    border-radius: 8px;
    margin: 5px 0;
  }
  .ai-message {
    text-align: left;
    background-color: #ffe0b2;
    padding: 8px;
    border-radius: 8px;
    margin: 5px 0;
  }
  .loading-indicator {
    font-style: italic;
    color: #555;
  }
  /* Additional styles for dropdowns and inputs */
  input[type=text], select {
    width: 60%;
    padding: 8px;
    margin-right: 10px;
    border-radius: 4px;
    border: 1px solid #ccc;
  }
  button {
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    background-color: #3aa4b4;
    color: white;
    cursor: pointer;
  }
  button:hover {
    background-color: #298a91;
  }
</style>
</head>
<body>

<header>
<h1>🌙 Telavista - Your Personal Learning Companion 🌙</h1>
<h3>✨ Empower your learning journey ✨</h3>
</header>

<!-- Tabs -->
<div class="tab">
  <button class="tablinks" onclick="showSection('AI')">🤖 AI</button>
  <button class="tablinks" onclick="showSection('PA')">🧑‍💼 P.A</button>
  <button class="tablinks" onclick="showSection('GPA')">%>5.0 GPA</button>
  <button class="tablinks" onclick="showSection('Goals')">🎯 Goals Road Map</button>
</div>

<!-- Sections -->
<div class="section" id="AI">
  <h3>Ask a Question</h3>
  <input type="text" id="aiUserInput" placeholder="Ask a question about anything..." />
  <button onclick="sendAsk('AI')">Ask</button>
  <div id="aiMessages"></div>
</div>

<div class="section" id="PA">
  <h3>Personal Assistant</h3>
  <input type="text" id="paUserInput" placeholder="Ask your Personal Assistant..." />
  <button onclick="sendAsk('PA')">Ask</button>
  <div id="paMessages"></div>
</div>

<div class="section" id="GPA">
  <h3>%>5.0 G.P.A</h3>
  <p>Ask about courses, studying tips, or anything related to GPA.</p>
  <input type="text" id="gpaUserInput" placeholder="Ask about GPA or courses..." />
  <select id="coursesDropdown">
    <option value="">Select a course</option>
    <option value="MATH101">Mathematics 101 - Calculus I</option>
    <option value="MATH102">Mathematics 102 - Calculus II</option>
    <option value="MATH103">Mathematics 103 - Linear Algebra</option>
    <option value="MATH104">Mathematics 104 - Discrete Mathematics</option>
    <option value="MATH105">Mathematics 105 - Probability & Statistics</option>
    <option value="MATH106">Mathematics 106 - Differential Equations</option>
    <option value="MATH107">Mathematics 107 - Mathematical Logic</option>
    <option value="MATH108">Mathematics 108 - Numerical Methods</option>
  </select>
  <button onclick="sendAsk('GPA')">Ask</button>
  <div id="gpaMessages"></div>
</div>

<div class="section" id="Goals">
  <h3>Goals Road Map</h3>
  <p>Ask about your goals, plans, or strategies to achieve them.</p>
  <input type="text" id="goalsUserInput" placeholder="Ask about your goals..." />
  <button onclick="sendAsk('Goals')">Ask</button>
  <div id="goalsMessages"></div>
</div>

<!-- JavaScript for tab switching and asking -->
<script>
  function showSection(sectionId) {
    document.querySelectorAll('.section').forEach(s => s.style.display='none');
    document.querySelectorAll('.tab button').forEach(b => b.classList.remove('active'));
    document.getElementById(sectionId).style.display='block';
    document.querySelector(`button[onclick="showSection('${sectionId}')"]`).classList.add('active');
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelector('.tab button').click();
  });

  async function sendAsk(section) {
    let inputId, messageId, question;
    if (section === 'AI') {
      inputId = 'aiUserInput'; messageId = 'aiMessages';
    } else if (section === 'PA') {
      inputId = 'paUserInput'; messageId = 'paMessages';
    } else if (section === 'GPA') {
      inputId = 'gpaUserInput'; messageId = 'gpaMessages';
    } else if (section === 'Goals') {
      inputId = 'goalsUserInput'; messageId = 'goalsMessages';
    } else return;

    question = document.getElementById(inputId).value.trim();
    if (!question) return;

    const messagesDiv = document.getElementById(messageId);
    // Show user's message
    const userMsg = document.createElement("div");
    userMsg.className = "user-message";
    userMsg.textContent = "You: " + question;
    messagesDiv.appendChild(userMsg);
    document.getElementById(inputId).value = "";
    messagesDiv.scrollTop = messagesDiv.scrollHeight;

    // For GPA section, include selected course if any
    let payloadQuestion = question;
    if (section === 'GPA') {
      const course = document.getElementById('coursesDropdown').value;
      if (course) {
        payloadQuestion += ` (Course: ${course})`;
      }
    }

    // Show loader
    const loadingMsg = document.createElement("div");
    loadingMsg.className = "loading-indicator";
    loadingMsg.textContent = "Telavista is thinking...";
    messagesDiv.appendChild(loadingMsg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;

    try {
      const res = await fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: payloadQuestion, section: section })
      });
      const data = await res.json();
      // Remove loader
      messagesDiv.removeChild(loadingMsg);
      const answer = data.answer || "Sorry, couldn't answer.";
      // Show response
      const aiMsg = document.createElement("div");
      aiMsg.className = "ai-message";
      aiMsg.innerHTML = "Telavista: " + answer;
      messagesDiv.appendChild(aiMsg);
      messagesDiv.scrollTop = messagesDiv.scrollHeight;
    } catch (err) {
      console.error("Error during API request:", err);
      messagesDiv.removeChild(loadingMsg);
      const errorMsg = document.createElement("div");
      errorMsg.textContent = "Error getting response.";
      messagesDiv.appendChild(errorMsg);
    }
  }
</script>

</body>
</html>
    """
    return HTMLResponse(content=html_content)

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")
    section = data.get("section", "")

    try:
        prompt = f"Section: {section}\nQuestion: {question}\nAnswer:"
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
        # Log the exception for debugging
        print(f"Error during DeepAI API call: {e}")
        answer = "Sorry, I couldn't generate a response at the moment."

    return JSONResponse({"answer": answer})
