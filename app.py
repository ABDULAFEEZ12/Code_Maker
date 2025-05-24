from fastapi import FastAPI 
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
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
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Telavista</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
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
            .cta-button {
                display: inline-block;
                margin-top: 20px;
                padding: 15px 30px;
                font-size: 1.2em;
                background-color: #3aa4b4;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
            }
            .cta-button:hover {
                background-color: #298a91;
            }
            section {
                max-width: 1000px;
                margin: 40px auto;
                padding: 0 20px;
            }
            h2 {
                color: #2b7a78;
                border-bottom: 2px solid #2b7a78;
                padding-bottom: 10px;
            }
            .feature {
                background-color: #ffffff;
                margin-top: 30px;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            .feature h3 {
                margin-top: 0;
                margin-bottom: 10px;
                color: #205d5a;
            }
            input[type="text"] {
                width: 100%;
                padding: 10px;
                margin-top: 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 1em;
            }
            /* Responsive improvements */
            @media(max-width: 600px){
                header h1 {
                    font-size: 2em;
                }
                .cta-button {
                    font-size: 1em;
                    padding: 10px 20px;
                }
            }
        </style>
    </head>
    <body>
        <header>
            <h1>🌍 TELAVISTA</h1>
            <p>The Future of Learning AI, Coding & Digital Skills – All in One Smart Platform.</p>
            <a href="#start" class="cta-button">Start Learning Now</a>
        </header>
        <section id="features">
            <!-- AI Assistant -->
            <div class="feature" id="ai-assistant">
                <h3>AI Assistant</h3>
                <p>Instant help with your coding problems and study questions using smart AI tools.</p>
                <input type="text" placeholder="Search AI help topics..." />
            </div>
            <!-- Code Playground -->
            <div class="feature" id="code-playground">
                <h3>Code Playground</h3>
                <p>Write, test and improve code in real time across Python, JavaScript, HTML, and more.</p>
                <input type="text" placeholder="Search code examples or languages..." />
            </div>
            <!-- Learning Paths -->
            <div class="feature" id="learning-paths">
                <h3>Learning Paths</h3>
                <p>Follow beginner-to-advanced paths to master programming, AI development, and data science.</p>
                <input type="text" placeholder="Search learning paths..." />
            </div>
            <!-- Courses & Challenges -->
            <div class="feature" id="courses-challenges">
                <h3>Courses & Challenges</h3>
                <p>Sharpen your skills with interactive challenges and tutorials designed for fast learning.</p>
                <input type="text" placeholder="Search courses or challenges..." />
            </div>
            <!-- Global Community -->
            <div class="feature" id="global-community">
                <h3>Global Community</h3>
                <p>Learn, share and build together with students and developers across the world.</p>
                <input type="text" placeholder="Search community topics..." />
            </div>
            <!-- Motivation Boost -->
            <div class="feature" id="motivation-boost">
                <h3>Motivation Boost</h3>
                <p>Daily coding streaks, reminders and motivational quotes to keep you consistent and focused.</p>
                <input type="text" placeholder="Search motivational content..." />
            </div>
        </section>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)                              templates/index.html  <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Telavista - Home</title>
<link rel="stylesheet" href="/static/styles.css" />
<style>
  /* Basic styles for tabs */
  body { font-family: Arial, sans-serif; margin: 0; }
  .tab {
    overflow: hidden;
    background-color: #333;
  }
  .tab button {
    background-color: inherit;
    float: left;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    transition: 0.3s;
    font-size: 17px;
  }
  .tab button:hover {
    background-color: #ddd;
  }
  .tab button.active {
    background-color: #2b7a78;
    color: white;
  }
  /* Content sections */
  .tabcontent {
    display: none;
    padding: 20px;
  }
</style>
</head>
<body>

<h2>Telavista</h2>
<div class="tab">
  <button class="tablinks" onclick="openTab(event, 'AI')">AI</button>
  <button class="tablinks" onclick="openTab(event, 'CodePlayground')">Code Playground</button>
  <button class="tablinks" onclick="openTab(event, 'StudyRoom')">Study Room</button>
  <button class="tablinks" onclick="openTab(event, 'GlobalCommunity')">Global Community</button>
</div>

<div id="AI" class="tabcontent">
  <!-- Inline content for AI -->
  <h3>AI Assistant</h3>
  <p>Get instant help with your coding problems and study questions using our smart AI tools.</p>
  <!-- Or load your AI page content here -->
</div>

<div id="CodePlayground" class="tabcontent">
  <h3>Code Playground</h3>
  <p>Write, test, and improve your code in real-time.</p>
</div>

<div id="StudyRoom" class="tabcontent">
  <h3>Study Room</h3>
  <p>Follow your learning paths to master programming, AI, and data science.</p>
</div>

<div id="GlobalCommunity" class="tabcontent">
  <h3>Global Community</h3>
  <p>Learn, share, and build with students and developers worldwide.</p>
</div>

<script>
function openTab(evt, tabName) {
  // Hide all tab content
  var tabcontent = document.getElementsByClassName("tabcontent");
  for (var i=0; i<tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  // Remove active class from all buttons
  var tablinks = document.getElementsByClassName("tablinks");
  for (var i=0; i<tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  // Show the selected tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}

// Open the first tab by default
document.addEventListener("DOMContentLoaded", () => {
  document.querySelector('.tablinks').click();
});
</script>

</body>
</html>
