from datetime import datetime

from pydantic import BaseModel, ConfigDict, HttpUrl

from app.models.enums import ApplicationStatus


class JobApplicationCreate(BaseModel):
    company_name: str
    job_role: str
    location: str
    date_applied: datetime
    status: ApplicationStatus
    job_url: HttpUrl

    recruiter_email: str | None = None
    notes: str | None = None
    salary: str | None = None
    source: str | None = None
    contact_person: str | None = None
    interview_date: datetime | None = None


class JobApplicationUpdate(BaseModel):
    company_name: str | None = None
    job_role: str | None = None
    location: str | None = None
    date_applied: datetime | None = None
    status: ApplicationStatus | None = None
    job_url: HttpUrl | None = None

    recruiter_email: str | None = None
    notes: str | None = None
    salary: str | None = None
    source: str | None = None
    contact_person: str | None = None
    interview_date: datetime | None = None


class JobApplicationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int

    company_name: str
    job_role: str
    location: str
    date_applied: datetime
    status: ApplicationStatus
    job_url: str

    recruiter_email: str | None
    notes: str | None
    salary: str | None
    source: str | None
    contact_person: str | None
    interview_date: datetime | None

    created_at: datetime
    updated_at: datetime