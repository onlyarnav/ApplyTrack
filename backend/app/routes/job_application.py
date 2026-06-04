from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_current_user
from app.db.database import get_db
from app.models.user import User
from app.schemas.job_application import (
    JobApplicationCreate,
    JobApplicationResponse,
    JobApplicationUpdate,
)
from app.services.job_application import (
    create_application,
    delete_application,
    get_application_by_id,
    get_applications,
    update_application,
)

router = APIRouter(
    prefix="/applications",
    tags=["applications"],
)


@router.post(
    "",
    response_model=JobApplicationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_job_application(
    payload: JobApplicationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_application(
        current_user.id,
        payload,
        db,
    )


@router.get(
    "",
    response_model=list[JobApplicationResponse],
)
def list_job_applications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_applications(
        current_user.id,
        db,
    )


@router.get(
    "/{application_id}",
    response_model=JobApplicationResponse,
)
def get_job_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    application = get_application_by_id(
        application_id,
        current_user.id,
        db,
    )

    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )

    return application


@router.put(
    "/{application_id}",
    response_model=JobApplicationResponse,
)
def update_job_application(
    application_id: int,
    payload: JobApplicationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    application = update_application(
        application_id,
        current_user.id,
        payload,
        db,
    )

    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )

    return application


@router.delete(
    "/{application_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_job_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    deleted = delete_application(
        application_id,
        current_user.id,
        db,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )

    return None