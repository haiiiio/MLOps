from fastapi import FastAPI
import uvicorn
import subprocess
import threading
import time
import sys

app = FastAPI(title="MLOps Class App")

@app.get("/")
def read_root():
    return {
        "message": "Welcome to MLOps Class",
        "ports": {
            "api": 8000,
            "dashboard": 8501
        },
        "instructions": [
            "API: http://localhost:8000",
            "Dashboard: http://localhost:8501 (if enabled)"
        ]
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": time.time()}

@app.get("/predict/{item_id}")
def predict(item_id: int):
    return {
        "item_id": item_id,
        "prediction": item_id * 0.5,
        "confidence": 0.95
    }

if __name__ == "__main__":
    print("Starting MLOps application...")
    print("API available on port 8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
