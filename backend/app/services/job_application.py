from sqlalchemy.orm import Session

from app.models.job_application import JobApplication
from app.schemas.job_application import (
    JobApplicationCreate,
    JobApplicationUpdate,
)


def create_application(
    user_id: int,
    payload: JobApplicationCreate,
    db: Session,
) -> JobApplication:
    application = JobApplication(
        user_id=user_id,
        **payload.model_dump(mode="json"),
    )

    db.add(application)
    db.commit()
    db.refresh(application)

    return application


def get_applications(
    user_id: int,
    db: Session,
) -> list[JobApplication]:
    return (
        db.query(JobApplication)
        .filter(JobApplication.user_id == user_id)
        .all()
    )


def get_application_by_id(
    application_id: int,
    user_id: int,
    db: Session,
) -> JobApplication | None:
    return (
        db.query(JobApplication)
        .filter(
            JobApplication.id == application_id,
            JobApplication.user_id == user_id,
        )
        .first()
    )


def update_application(
    application_id: int,
    user_id: int,
    payload: JobApplicationUpdate,
    db: Session,
) -> JobApplication | None:
    application = get_application_by_id(
        application_id,
        user_id,
        db,
    )

    if application is None:
        return None

    update_data = payload.model_dump(
        mode="json",
        exclude_unset=True,
    )

    for field, value in update_data.items():
        setattr(application, field, value)

    db.commit()
    db.refresh(application)

    return application


def delete_application(
    application_id: int,
    user_id: int,
    db: Session,
) -> bool:
    application = get_application_by_id(
        application_id,
        user_id,
        db,
    )

    if application is None:
        return False

    db.delete(application)
    db.commit()

    return True