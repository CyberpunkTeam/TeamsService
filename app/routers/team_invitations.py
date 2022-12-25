import os
from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.team_invitations_controller import TeamInvitationsController
from app.models.requests.team_invitations_update import TeamInvitationsUpdate
from app.models.team_invitations import TeamInvitations
from app.models.teams import Teams
from app.repositories.team_invitations_repository import TeamInvitationsRepository

router = APIRouter()

# Repository
team_invitations_repository = TeamInvitationsRepository(
    config.DATABASE_URL, config.DATABASE_NAME
)


@router.post("/team_invitations/reset", tags=["team_invitations"], status_code=200)
async def reset():
    if os.environ.get("TEST_MODE") == "1":
        return {"reset": team_invitations_repository.reset()}


@router.post(
    "/team_invitations/",
    tags=["teams"],
    response_model=TeamInvitations,
    status_code=201,
)
async def create_team_invitations(team_invitation: TeamInvitations):
    return TeamInvitationsController.post(team_invitations_repository, team_invitation)


@router.get("/team_invitations/", tags=["teams"], response_model=List[TeamInvitations])
async def list_team_invitations(
    tid: str = None, postulant_uid: str = None, team_owner_uid: str = None
):
    return TeamInvitationsController.get(
        team_invitations_repository,
        tid=tid,
        team_owner_uid=team_owner_uid,
        postulant_uid=postulant_uid,
    )


@router.get("/team_invitations/{tiid}", tags=["teams"], response_model=TeamInvitations)
async def read_team_invitations(tiid: str):
    return TeamInvitationsController.get(team_invitations_repository, tiid=tiid)


@router.put("/team_invitations/{tiid}", tags=["teams"], response_model=TeamInvitations)
async def update_team_invitations(tiid: str, team_invitation: TeamInvitationsUpdate):
    return TeamInvitationsController.update(
        team_invitations_repository, tiid, team_invitation
    )
