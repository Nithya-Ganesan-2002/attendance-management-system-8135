from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field

from src.api.dependencies import get_settings, Settings

router = APIRouter(prefix="/auth", tags=["Authentication"])


class LoginRequest(BaseModel):
    """Login payload with email/password."""

    email: str = Field(..., description="User email address")
    password: str = Field(..., description="User password")


class LoginResponse(BaseModel):
    """Login response with access token placeholder."""

    access_token: str = Field(..., description="JWT access token (placeholder)")
    token_type: str = Field("bearer", description="Type of token")


class MeResponse(BaseModel):
    """User profile information placeholder."""

    id: str = Field(..., description="User ID")
    email: str = Field(..., description="Email address")
    role: Optional[str] = Field(None, description="User role if available")


@router.post(
    "/login",
    response_model=LoginResponse,
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    summary="Login",
    description="Authenticate user against Supabase. Currently a stub returning 501 Not Implemented.",
    responses={
        501: {"description": "Not Implemented"},
        400: {"description": "Bad Request"},
        500: {"description": "Server configuration error"},
    },
)
def login(payload: LoginRequest, settings: Settings = Depends(get_settings)) -> LoginResponse:
    """Attempt login via Supabase (stub). Returns 501 with TODO."""
    # Ensure configuration exists when we actually need it
    settings.require()

    # Placeholder behavior
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="TODO: Implement Supabase email/password login",
    )


@router.get(
    "/me",
    response_model=MeResponse,
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    summary="Get current user",
    description="Retrieve currently authenticated user. Currently a stub returning 501 Not Implemented.",
    responses={
        501: {"description": "Not Implemented"},
        401: {"description": "Unauthorized"},
        500: {"description": "Server configuration error"},
    },
)
def get_me(settings: Settings = Depends(get_settings)) -> MeResponse:
    """Get current authenticated user (stub)."""
    settings.require()
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="TODO: Implement user retrieval from Supabase JWT",
    )
