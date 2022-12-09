from http.client import HTTPException

import mongomock
import pytest

from app import config
from app.models.teams import Teams
from app.repositories.teams_repository import TeamsRepository


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_save_teams():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = TeamsRepository(url, db_name)

    team = Teams(
        name="GreenTeam",
        tid="4211",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
        owner="1234",
    )

    ok = repository.insert(team)

    assert ok


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_team():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = TeamsRepository(url, db_name)

    team = Teams(
        name="GreenTeam",
        tid="4211",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
        owner="1234",
    )

    ok = repository.insert(team)

    assert ok

    teams_found = repository.get("4211")

    assert len(teams_found) == 1

    team_found = teams_found[0]

    assert team_found.name == "GreenTeam"
    assert team_found.tid == "4211"
    assert team_found.technologies == ["Python", "React"]
    assert team_found.project_preferences == ["web", "AI", "Crypto"]
    assert team_found.owner == "1234"


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_error_team_name_exists():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = TeamsRepository(url, db_name)

    team = Teams(
        name="GreenTeam",
        tid="4211",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
        owner="1234",
    )

    ok = repository.insert(team)

    assert ok

    assert repository.exists(team)


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_filter_members_by_uid():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = TeamsRepository(url, db_name)

    team = Teams(
        name="GreenTeam",
        tid="444",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
        owner="123444",
    )

    repository.insert(team)
    new_mid = "44545"
    team = Teams(
        name="GreenTeam",
        tid="4211",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
        owner="1234",
        members=["4211", new_mid],
    )

    repository.insert(team)

    found = repository.get(uid=new_mid)

    assert len(found) == 1
