from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field

from src.api.dependencies import get_settings, Settings

router = APIRouter(prefix="/attendance", tags=["Attendance"])


class MarkAttendanceRequest(BaseModel):
    """Payload to mark attendance for a student in a class."""

    class_id: str = Field(..., description="Class ID")
    student_id: str = Field(..., description="Student ID")
    status: str = Field(..., description="Attendance status e.g., present, absent, late")
    timestamp: Optional[datetime] = Field(None, description="Optional custom timestamp")


class AttendanceRecord(BaseModel):
    """Attendance record entry."""

    id: str = Field(..., description="Record ID")
    class_id: str = Field(..., description="Class ID")
    student_id: str = Field(..., description="Student ID")
    status: str = Field(..., description="Status")
    timestamp: datetime = Field(..., description="Timestamp of mark")


@router.post(
    "/mark",
    response_model=AttendanceRecord,
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    summary="Mark attendance",
    description="Mark attendance for a student. Currently a stub returning 501 Not Implemented.",
    responses={
        501: {"description": "Not Implemented"},
        400: {"description": "Bad Request"},
        500: {"description": "Server configuration error"},
    },
)
def mark_attendance(payload: MarkAttendanceRequest, settings: Settings = Depends(get_settings)) -> AttendanceRecord:
    """Mark attendance (stub)."""
    settings.require()
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="TODO: Implement attendance marking in Supabase",
    )


@router.get(
    "/history",
    response_model=List[AttendanceRecord],
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    summary="Attendance history",
    description="Fetch attendance history. Currently a stub returning 501 Not Implemented.",
    responses={501: {"description": "Not Implemented"}, 500: {"description": "Server configuration error"}},
)
def attendance_history(
    class_id: Optional[str] = None,
    student_id: Optional[str] = None,
    settings: Settings = Depends(get_settings),
) -> list[AttendanceRecord]:
    """Get attendance history (stub)."""
    settings.require()
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="TODO: Implement fetching attendance history from Supabase",
    )
