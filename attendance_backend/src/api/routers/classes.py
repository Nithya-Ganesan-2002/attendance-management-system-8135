from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field

from src.api.dependencies import get_settings, Settings

router = APIRouter(prefix="/classes", tags=["Classes"])


class ClassModel(BaseModel):
    """Representation of a class/course."""

    id: str = Field(..., description="Class unique identifier")
    name: str = Field(..., description="Class name")
    description: str | None = Field(None, description="Class description")


class CreateClassRequest(BaseModel):
    """Create a new class/course."""

    name: str = Field(..., description="Class name")
    description: str | None = Field(None, description="Class description")


@router.get(
    "",
    response_model=List[ClassModel],
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    summary="List classes",
    description="List available classes. Currently a stub returning 501 Not Implemented.",
    responses={501: {"description": "Not Implemented"}, 500: {"description": "Server configuration error"}},
)
def list_classes(settings: Settings = Depends(get_settings)) -> list[ClassModel]:
    """List classes (stub)."""
    settings.require()
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="TODO: Implement listing classes from Supabase",
    )


@router.post(
    "",
    response_model=ClassModel,
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    summary="Create class",
    description="Create a new class. Currently a stub returning 501 Not Implemented.",
    responses={
        501: {"description": "Not Implemented"},
        400: {"description": "Bad Request"},
        500: {"description": "Server configuration error"},
    },
)
def create_class(payload: CreateClassRequest, settings: Settings = Depends(get_settings)) -> ClassModel:
    """Create a new class (stub)."""
    settings.require()
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="TODO: Implement class creation in Supabase",
    )
