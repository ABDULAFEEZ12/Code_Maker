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
    return HTMLResponse(content=html_content)
