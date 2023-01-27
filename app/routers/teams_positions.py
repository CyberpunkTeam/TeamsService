import os
from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.teams_positions import TeamsPositionsController
from app.models.requests.team_position_update import TeamPositionUpdate
from app.models.teams_positions import TeamsPositions
from app.repositories.teams_positions_repository import TeamsPositionsRepository
from app.routers.teams import teams_repository

router = APIRouter()

# Repository
teams_positions_repository = TeamsPositionsRepository(
    config.DATABASE_URL, config.DATABASE_NAME
)


@router.post("/teams_positions/reset", tags=["teams"], status_code=200)
async def reset():
    if os.environ.get("TEST_MODE") == "1":
        return {"reset": teams_positions_repository.reset()}


@router.post(
    "/teams_positions/",
    tags=["teams_positions"],
    response_model=TeamsPositions,
    status_code=201,
)
async def create_team_position(teams_positions: TeamsPositions):
    return TeamsPositionsController.post(teams_positions_repository, teams_positions)


@router.get(
    "/teams_positions/",
    tags=["teams_positions"],
    response_model=List[TeamsPositions],
)
async def list_team_positions(tid: str = None, state: str = None):
    return TeamsPositionsController.get(
        teams_positions_repository, teams_repository, tid=tid, state=state
    )


@router.get(
    "/teams_positions/{tpid}",
    tags=["teams_positions"],
    response_model=TeamsPositions,
)
async def get_team_positions(tpid: str = None):
    return TeamsPositionsController.get(teams_positions_repository, tpid=tpid)


@router.post(
    "/teams_positions/{tpid}/candidates/{uid}",
    tags=["teams_positions"],
    response_model=TeamsPositions,
)
async def add_candidate(tpid: str = None, uid: str = None):
    return TeamsPositionsController.add_candidate(
        teams_positions_repository, tpid=tpid, candidate_id=uid
    )


@router.put("/teams_positions/{tpid}", tags=["teams"], response_model=TeamsPositions)
async def update_user(tpid: str, team_position: TeamPositionUpdate):
    return TeamsPositionsController.put(teams_positions_repository, tpid, team_position)
