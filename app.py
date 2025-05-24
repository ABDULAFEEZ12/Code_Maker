from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (adjust origins in production)
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
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Telavista</title>
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
            .tabcontent {
                display: none;
                padding: 20px;
                background-color: #fff;
                margin: 20px auto;
                max-width: 1000px;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            .tabcontent h3 {
                color: #205d5a;
            }
        </style>
    </head>
    <body>

        <header>
            <h1>🌍 TELAVISTA</h1>
            <p>The Future of Learning AI, Coding & Digital Skills – All in One Smart Platform.</p>
            <a href="#tabs" class="cta-button">Start Learning Now</a>
        </header>

        <div class="tab" id="tabs">
            <button class="tablinks" onclick="openTab(event, 'AI')">AI</button>
            <button class="tablinks" onclick="openTab(event, 'CodePlayground')">Code Playground</button>
            <button class="tablinks" onclick="openTab(event, 'StudyRoom')">Study Room</button>
            <button class="tablinks" onclick="openTab(event, 'GlobalCommunity')">Global Community</button>
        </div>

        <div id="AI" class="tabcontent">
            <h3>AI</h3>
            <p>Get instant help with your coding problems and study questions using our smart AI tools.</p>
        </div>

        <div id="Personal_Assistant" class="tabcontent">
            <h3>Personal Assistant</h3>
            <p>Write, test, and improve TELLA ABDUL AFEEZ ADEWALE in real-time.</p>
        </div>

        <div id="5.0GPA" class="tabcontent">
            <h3>%>5.0 G.P.A</h3>
            <p>Follow your learning paths to master programming, AI, and data science.</p>
        </div>

        <div id="GoalsRoadMap" class="tabcontent">
            <h3>Goals Road-Map</h3>
            <p>How Tella Abdul Afeez Adewale will rule the WORLD.</p>
        </div>

        <script>
            function openTab(evt, tabName) {
                var i, tabcontent, tablinks;
                tabcontent = document.getElementsByClassName("tabcontent");
                for (i = 0; i < tabcontent.length; i++) {
                    tabcontent[i].style.display = "none";
                }
                tablinks = document.getElementsByClassName("tablinks");
                for (i = 0; i < tablinks.length; i++) {
                    tablinks[i].className = tablinks[i].className.replace(" active", "");
                }
                document.getElementById(tabName).style.display = "block";
                evt.currentTarget.className += " active";
            }
            // Auto open first tab
            document.addEventListener("DOMContentLoaded", () => {
                document.querySelector(".tablinks").click();
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
