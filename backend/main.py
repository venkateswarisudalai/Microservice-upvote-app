from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import threading

app = FastAPI(title="Engagement Analytics Backend")

# Enable CORS so the frontend web app can communicate with this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LikeDatabase:
    def __init__(self):
        self.count = 0
        self._lock = threading.Lock()
        
    def increment(self):
        with self._lock:
            self.count += 1
            return self.count
            
    def get_count(self):
        return self.count

db = LikeDatabase()

@app.get("/api/likes")
def get_likes():
    return {"likes": db.get_count()}

@app.post("/api/likes")
def add_like():
    return {"likes": db.increment()}