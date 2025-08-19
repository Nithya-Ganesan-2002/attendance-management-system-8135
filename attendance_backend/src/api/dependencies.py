import os
from functools import lru_cache
from typing import Optional

from fastapi import HTTPException, status


class Settings:
    """Application settings loaded from environment variables for Supabase and other configs."""

    def __init__(
        self,
        supabase_url: Optional[str],
        supabase_anon_key: Optional[str],
        supabase_service_role_key: Optional[str],
        supabase_jwt_secret: Optional[str],
        environment: str = "development",
    ) -> None:
        self.SUPABASE_URL = supabase_url
        self.SUPABASE_ANON_KEY = supabase_anon_key
        self.SUPABASE_SERVICE_ROLE_KEY = supabase_service_role_key
        self.SUPABASE_JWT_SECRET = supabase_jwt_secret
        self.ENVIRONMENT = environment

    def validate_required(self) -> None:
        """Validate that core Supabase settings exist. For now, we don't fail on startup to allow CI/docs."""
        missing = []
        if not self.SUPABASE_URL:
            missing.append("SUPABASE_URL")
        if not self.SUPABASE_ANON_KEY:
            missing.append("SUPABASE_ANON_KEY")
        if not self.SUPABASE_SERVICE_ROLE_KEY:
            missing.append("SUPABASE_SERVICE_ROLE_KEY")
        if not self.SUPABASE_JWT_SECRET:
            missing.append("SUPABASE_JWT_SECRET")
        # We do not raise here to keep the app bootable and OpenAPI generatable without secrets.
        # Individual endpoints may still check and raise if needed.
        self._missing = missing  # store for diagnostics

    def require(self) -> None:
        """Raise HTTP 500 if critical settings are missing when an endpoint actually needs them."""
        if getattr(self, "_missing", []):
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    "message": "Server is not fully configured. Missing environment variables.",
                    "missing": getattr(self, "_missing", []),
                },
            )


# PUBLIC_INTERFACE
@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Get cached Settings constructed from environment variables."""
    settings = Settings(
        supabase_url=os.getenv("SUPABASE_URL"),
        supabase_anon_key=os.getenv("SUPABASE_ANON_KEY"),
        supabase_service_role_key=os.getenv("SUPABASE_SERVICE_ROLE_KEY"),
        supabase_jwt_secret=os.getenv("SUPABASE_JWT_SECRET"),
        environment=os.getenv("ENVIRONMENT", "development"),
    )
    settings.validate_required()
    return settings
