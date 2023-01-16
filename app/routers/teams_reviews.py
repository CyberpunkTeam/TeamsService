import os
from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.teams_reviews_controller import TeamsReviewsController
from app.models.teams_reviews import TeamsReviews
from app.repositories.teams_reviews_repository import TeamsReviewsRepository


router = APIRouter()

# Repository
projects_reviews_repository = TeamsReviewsRepository(
    config.DATABASE_URL, config.DATABASE_NAME
)


@router.post(
    "/teams_reviews/",
    tags=["teams_reviews"],
    response_model=TeamsReviews,
    status_code=201,
)
async def create_team_review(project_review: TeamsReviews):
    return TeamsReviewsController.post(projects_reviews_repository, project_review)


@router.get(
    "/teams_reviews/",
    tags=["teams_reviews"],
    response_model=List[TeamsReviews],
)
async def list_team_reviews(pid: str = None, tid: str = None):
    return TeamsReviewsController.get(projects_reviews_repository, pid=pid, tid=tid)
