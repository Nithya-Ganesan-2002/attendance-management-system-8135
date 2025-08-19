from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routers.auth import router as auth_router
from src.api.routers.classes import router as classes_router
from src.api.routers.attendance import router as attendance_router

openapi_tags = [
    {"name": "Health", "description": "Service health and status"},
    {"name": "Authentication", "description": "Authentication and user session management"},
    {"name": "Classes", "description": "Class management operations"},
    {"name": "Attendance", "description": "Attendance operations"},
]

app = FastAPI(
    title="Attendance Management API",
    description=(
        "APIs for authentication, class management, and attendance tracking. "
        "Supabase integration is planned; current endpoints are stubbed (501) where applicable."
    ),
    version="0.1.0",
    openapi_tags=openapi_tags,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"], summary="Health Check")
def health_check():
    """Basic health check endpoint to verify the service is running."""
    return {"message": "Healthy"}


# Mount versioned API routers under /api
app.include_router(auth_router, prefix="/api")
app.include_router(classes_router, prefix="/api")
app.include_router(attendance_router, prefix="/api")
