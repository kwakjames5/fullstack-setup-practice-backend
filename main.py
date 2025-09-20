from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Configure CORS for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Local development
        "fullstack-setup-practice-frontend-5orv1icqf.vercel.app",  # Updated to not have trailing /, deployment URL
        "https://fullstack-setup-practice-frontend.vercel.app/", # domain url
        "https://*.vercel.app",   # All Vercel deployments
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI!"}

@app.get("/api/health")
async def health():
    return {"status": "healthy", "environment": os.getenv("ENVIRONMENT", "development")}