from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="Engagement Analytics Frontend")
BACKEND_URL = os.getenv("BACKEND_API_URL", "http://localhost:8080")

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud-Native Engagement Platform</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #121212; color: white; text-align: center; padding-top: 80px; margin: 0; }}
            .card {{ background: #1e1e1e; padding: 30px; border-radius: 15px; display: inline-block; max-width: 400px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #333; }}
            img {{ width: 100%; border-radius: 10px; border: 1px solid #444; }}
            .count {{ font-size: 28px; color: #00ffcc; margin: 20px 0; font-weight: bold; }}
            button {{ background: #ff007f; color: white; border: none; padding: 12px 30px; font-size: 18px; border-radius: 25px; cursor: pointer; font-weight: bold; width: 100%; transition: transform 0.1s; }}
            button:hover {{ background: #e0006c; transform: scale(1.02); }}
            button:active {{ transform: scale(0.98); }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Live GitOps Platform Demo</h2>
            <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500" alt="Abstract Canvas">
            <div class="count">❤️ <span id="like-cnt">0</span> Likes</div>
            <button onclick="registerLike()">Like Photo</button>
        </div>
        <script>
            const backendEndpoint = "{BACKEND_URL}";
            
            async function getLikes() {{
                try {{
                    const res = await fetch(`${{backendEndpoint}}/api/likes`);
                    const data = await res.json();
                    document.getElementById('like-cnt').innerText = data.likes;
                }} catch (err) {{ console.error("Backend unreachable", err); }}
            }}
            
            async function registerLike() {{
                try {{
                    const res = await fetch(`${{backendEndpoint}}/api/likes`, {{ method: 'POST' }});
                    const data = await res.json();
                    document.getElementById('like-cnt').innerText = data.likes;
                }} catch (err) {{ console.error("Failed to register like", err); }}
            }}
            getLikes();
        </script>
    </body>
    </html>
    """