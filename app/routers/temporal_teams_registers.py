from typing import List
from fastapi import APIRouter
from app import config
from app.controllers.temporal_teams_registers_controller import (
    TemporalTeamsRegistersController,
)
from app.models.temporal_teams_registers import TemporalTeamsRegisters
from app.repositories.temporal_teams_registers_repository import (
    TemporalTeamsRegistersRepository,
)

router = APIRouter()

# Repository
temporal_projects_registers_repository = TemporalTeamsRegistersRepository(
    config.DATABASE_URL, config.DATABASE_NAME
)


@router.post(
    "/temporal_teams_registers/",
    tags=["temporal_teams_registers"],
    response_model=TemporalTeamsRegisters,
    status_code=201,
)
async def create_team_review(temporal_team_register: TemporalTeamsRegisters):
    return TemporalTeamsRegistersController.post(
        temporal_projects_registers_repository, temporal_team_register
    )


@router.get(
    "/temporal_teams_registers/",
    tags=["temporal_teams_registers"],
    response_model=List[TemporalTeamsRegisters],
)
async def list_team_reviews(pid: str = None, tid: str = None):
    return TemporalTeamsRegistersController.get(
        temporal_projects_registers_repository, pid=pid, tid=tid
    )
