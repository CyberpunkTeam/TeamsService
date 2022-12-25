from fastapi import FastAPI
from .routers import teams, state, team_invitations


app = FastAPI()


app.include_router(teams.router)
app.include_router(state.router)
app.include_router(team_invitations.router)
