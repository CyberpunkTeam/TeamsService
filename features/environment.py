from app.main import app
from behave import fixture, use_fixture
import os
from fastapi.testclient import TestClient


# Crea una variable para poder hacer llamadas a la API
@fixture
def app_client(context, *args, **kwargs):
    os.environ["TEST_MODE"] = "1"
    context.client = TestClient(app)
    yield context.client


# Hooks para hacer Rollbacks y setear variable de entorno de test
def before_all(context):
    os.environ["TEST_MODE"] = "1"


#
#
def before_feature(context, feature):
    use_fixture(app_client, context)
    context.vars = (
        {}
    )  # Rollback de variables entre feature (vars permite compartir variables entre steps)
    context.client.post("/teams/reset")
    context.client.post("/team_invitations/reset")


#


def after_scenario(context, scenario):
    context.client.post("/teams/reset")
    context.client.post("/team_invitations/reset")
    context.client.post("/teams_positions/reset")


#
# def after_all(context):
#     del os.environ["TEST_MODE"]
