from fastapi import FastAPI
from app.main import app as app_router

# Create main FastAPI app
app = FastAPI()

# Include the main router
app.include_router(app_router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "PortfolioAI API is running"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
