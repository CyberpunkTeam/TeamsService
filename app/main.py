from fastapi import FastAPI
from .routers import (
    teams,
    state,
    team_invitations,
    teams_reviews,
    team_members_reviews,
    teams_positions,
    temporal_teams_registers,
)


app = FastAPI()


app.include_router(teams.router)
app.include_router(state.router)
app.include_router(team_invitations.router)
app.include_router(teams_reviews.router)
app.include_router(team_members_reviews.router)
app.include_router(teams_positions.router)
app.include_router(temporal_teams_registers.router)
