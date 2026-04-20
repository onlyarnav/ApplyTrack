from __future__ import annotations
from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..models.enums import ApplicationStatus
from ..db.database import Base

class JobApplication(Base):
    __tablename__ = "job_applications"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)

    company_name: Mapped[str] = mapped_column(index=True)
    job_role: Mapped[str] = mapped_column(index=True)
    location: Mapped[str] = mapped_column()
    date_applied: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )
    status: Mapped[str] = mapped_column(
        SAEnum(ApplicationStatus, name="applicationstatus"),
        index=True
    )
    job_url: Mapped[str] = mapped_column()

    recruiter_email: Mapped[str | None] = mapped_column()
    notes: Mapped[str | None] = mapped_column(Text)
    salary: Mapped[str | None] = mapped_column()
    source: Mapped[str | None] = mapped_column()
    contact_person: Mapped[str | None] = mapped_column()
    interview_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )

    user: Mapped["User"] = relationship(back_populates="job_applications")