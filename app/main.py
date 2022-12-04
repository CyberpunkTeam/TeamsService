from fastapi import FastAPI
from .routers import teams, state


app = FastAPI()


app.include_router(teams.router)
app.include_router(state.router)
