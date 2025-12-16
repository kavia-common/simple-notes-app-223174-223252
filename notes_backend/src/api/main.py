from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.notes import router as notes_router

# Create FastAPI app with metadata and tags
app = FastAPI(
    title="Simple Notes API",
    description="A simple FastAPI backend for managing notes with in-memory storage.",
    version="0.1.0",
    openapi_tags=[
        {"name": "health", "description": "Health check endpoint"},
        {"name": "notes", "description": "CRUD operations for notes"},
    ],
)

# CORS configuration: allow localhost origins for dev and preview
allowed_origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "http://0.0.0.0",
    "http://0.0.0.0:3000",
    "*",  # keep permissive for preview; restrict later as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["health"], summary="Health Check")
def health_check():
    """
    PUBLIC_INTERFACE
    Health check endpoint.

    Returns a simple JSON payload indicating the service is up.
    """
    return {"message": "Healthy"}


# Include notes router
app.include_router(notes_router, prefix="/notes", tags=["notes"])


# Uvicorn entrypoint note:
# The container runtime starts the server binding to port 3001 externally.
# If running locally: `uvicorn src.api.main:app --host 0.0.0.0 --port 3001 --reload`
