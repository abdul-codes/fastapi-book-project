import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from api.router import api_router
from core.config import settings


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_PREFIX)


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)