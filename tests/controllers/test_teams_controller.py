from unittest.mock import Mock

import mongomock
import pytest
from fastapi import HTTPException

from app.controllers.teams_controller import TeamsController
from app.models.teams import Teams
from app.repositories.teams_repository import TeamsRepository


def test_get_all_teams():
    repository = Mock()
    repository.get.return_value = [
        Teams(
            name="GreenTeam",
            tid="1234",
            technologies=["Python", "React"],
            project_preferences=["web", "AI", "Crypto"],
            owner="1234",
        ),
        Teams(
            name="VitalikArmy",
            tid="3333",
            technologies=["Python", "TS"],
            project_preferences=["web3", "Crypto"],
            owner="1234",
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
            owner="1234",
        ),
        Teams(
            name="VitalikArmy",
            tid="4313",
            technologies=["Python", "TS"],
            project_preferences=["web3", "Crypto"],
            owner="1234",
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
            owner="1234",
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
    repository.exists.return_value = False
    repository.insert.return_value = True
    team = Teams(
        name="GreenTeam",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
        owner="1234",
    )

    result = TeamsController.post(repository, team)
    assert result == team
    assert result.tid is not None


def test_error_create_team():
    repository = Mock()
    repository.exists.return_value = False
    repository.insert.return_value = False
    team = Teams(
        name="GreenTeam",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
        owner="1234",
    )
    with pytest.raises(HTTPException):
        TeamsController.post(repository, team)


def test_error_team_name_exists():
    repository = Mock()
    repository.exists.return_value = True
    team = Teams(
        name="GreenTeam",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
        owner="1234",
    )
    with pytest.raises(HTTPException):
        TeamsController.post(repository, team)


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_add_member_to_team():
    team = Teams(
        name="GreenTeam",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
        owner="1234",
    )
    repository = TeamsRepository("server.example.com", "test")
    result = TeamsController.post(repository, team)

    assert len(result.members) == 1

    new_member = "12355"
    TeamsController.add_member(repository, result.tid, new_member)

    team_returned = TeamsController.get(repository, result.tid, top=True)
    assert len(team_returned.members) == 2


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_teams_by_owner():
    owner_1 = "1234"
    owner_2 = "5678"
    team_1 = Teams(
        name="GreenTeam 1",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
        owner=owner_1,
    )
    team_2 = Teams(
        name="GreenTeam 2",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
        owner=owner_2,
    )
    team_3 = Teams(
        name="GreenTeam 3",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
        owner=owner_1,
    )
    repository = TeamsRepository("server.example.com", "test")
    TeamsController.post(repository, team_1)
    TeamsController.post(repository, team_2)
    TeamsController.post(repository, team_3)

    teams_owner_1 = TeamsController.get(repository, owner=owner_1)
    teams_owner_2 = TeamsController.get(repository, owner=owner_2)

    assert len(teams_owner_1) == 2
    assert len(teams_owner_2) == 1
