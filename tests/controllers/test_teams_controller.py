from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from app.controllers.teams_controller import TeamsController
from app.models.teams import Teams


def test_get_all_teams():
    repository = Mock()
    repository.get.return_value = [
        Teams(
            name="GreenTeam",
            tid="1234",
            technologies=["Python", "React"],
            project_preferences=["web", "AI", "Crypto"],
        ),
        Teams(
            name="VitalikArmy",
            tid="3333",
            technologies=["Python", "TS"],
            project_preferences=["web3", "Crypto"],
        ),
    ]
    result = TeamsController.get(repository)
    assert len(result) == 2


def test_get_top_team():
    repository = Mock()
    repository.get.return_value = [
        Teams(
            name="GreenTeam",
            tid="4211",
            technologies=["Python", "React"],
            project_preferences=["web", "AI", "Crypto"],
        ),
        Teams(
            name="VitalikArmy",
            tid="4313",
            technologies=["Python", "TS"],
            project_preferences=["web3", "Crypto"],
        ),
    ]
    result = TeamsController.get(repository, top=True)
    assert result.name == "GreenTeam"


def test_get_team():
    repository = Mock()
    repository.get.return_value = [
        Teams(
            name="GreenTeam",
            tid="4211",
            technologies=["Python", "React"],
            project_preferences=["web", "AI", "Crypto"],
        )
    ]
    result = TeamsController.get(repository, tid="4211", top=True)
    assert result.name == "GreenTeam"


def test_error_team_not_found():
    repository = Mock()
    repository.get.return_value = []
    with pytest.raises(HTTPException):
        TeamsController.get(repository, tid="4211", top=True)


def test_create_team():
    repository = Mock()
    repository.insert.return_value = True
    team = Teams(
        name="GreenTeam",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
    )

    result = TeamsController.post(repository, team)
    assert result == team
    assert result.tid is not None


def test_error_create_team():
    repository = Mock()
    repository.insert.return_value = False
    team = Teams(
        name="GreenTeam",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
    )
    with pytest.raises(HTTPException):
        TeamsController.post(repository, team)
