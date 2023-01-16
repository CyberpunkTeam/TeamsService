from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.team_members_reviews_controller import TeamMembersReviewsController
from app.models.team_members_reviews import TeamMembersReviews
from app.models.teams_reviews import TeamsReviews
from app.repositories.team_members_reviews_repository import (
    TeamMembersReviewsRepository,
)

router = APIRouter()

# Repository
team_members_reviews_repository = TeamMembersReviewsRepository(
    config.DATABASE_URL, config.DATABASE_NAME
)


@router.post(
    "/team_members_reviews/",
    tags=["teams_reviews"],
    response_model=TeamsReviews,
    status_code=201,
)
async def create_team_member_review(team_member_review: TeamMembersReviews):
    return TeamMembersReviewsController.post(
        team_members_reviews_repository, team_member_review
    )


@router.get(
    "/team_members_reviews/",
    tags=["teams_reviews"],
    response_model=List[TeamsReviews],
)
async def list_team_member_review(
    pid: str = None,
    tid: str = None,
    member_reviewer: str = None,
    member_reviewed: str = None,
):
    return TeamMembersReviewsController.get(
        team_members_reviews_repository,
        pid=pid,
        tid=tid,
        member_reviewer=member_reviewer,
        member_reviewed=member_reviewed,
    )
