from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.teams_controller import TeamsController
from app.models.teams import Teams
from app.repositories.teams_repository import TeamsRepository

router = APIRouter()

# Repository
teams_repository = TeamsRepository(config.DATABASE_URL, config.DATABASE_NAME)


@router.post("/teams/", tags=["teams"], response_model=Teams, status_code=201)
async def create_team(team: Teams):
    return TeamsController.post(teams_repository, team)


@router.get("/teams/", tags=["teams"], response_model=List[Teams])
async def list_team():
    return TeamsController.get(teams_repository)


@router.get("/teams/{tid}", tags=["teams"], response_model=Teams)
async def read_team(tid: str):
    return TeamsController.get(teams_repository, tid, top=True)
