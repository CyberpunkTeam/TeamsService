import os
from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.responses import Message
from app.controllers.teams_controller import TeamsController
from app.models.requests.team_update import TeamUpdate
from app.models.teams import Teams
from app.repositories.teams_repository import TeamsRepository

router = APIRouter()

# Repository
teams_repository = TeamsRepository(config.DATABASE_URL, config.DATABASE_NAME)


@router.post("/teams/reset", tags=["teams"], status_code=200)
async def reset():
    if os.environ.get("TEST_MODE") == "1":
        return {"reset": teams_repository.reset()}


@router.post("/teams/", tags=["teams"], response_model=Teams, status_code=201)
async def create_team(team: Teams):
    return TeamsController.post(teams_repository, team)


@router.get("/teams/", tags=["teams"], response_model=List[Teams])
async def list_team(
    mid: str = None, search: str = None, owner: str = None, tids: str = None
):
    if search is not None:
        return TeamsController.search(teams_repository, search)

    if tids is not None:
        tids = tids[1 : len(tids) - 1].split(",")

        return TeamsController.get(teams_repository, tids=tids)

    return TeamsController.get(teams_repository, uid=mid, owner=owner)


@router.get("/teams/{tid}", tags=["teams"], response_model=Teams)
async def read_team(tid: str):
    return TeamsController.get(teams_repository, tid, top=True)


@router.put("/teams/{tid}", tags=["teams"], response_model=Teams)
async def update_user(tid: str, team: TeamUpdate):
    return TeamsController.put(teams_repository, tid, team)


@router.post(
    "/teams/{tid}/members/{mid}",
    tags=["teams"],
    response_model=Message,
    status_code=201,
)
async def create_team_member(tid: str, mid: str):
    return TeamsController.add_member(teams_repository, tid, mid)


@router.get("/metrics", tags=["metrics"], status_code=200)
async def get_metrics():
    return TeamsController.get_metrics(teams_repository)
