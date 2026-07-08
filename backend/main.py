from fastapi import FastAPI

app = FastAPI(
    title="CIOS",
    description="Career Intelligence Operating System",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "status": "running",
        "project": "CIOS"
    }

@app.get("/health")
def health():
    return {
        "healthy": True
    }