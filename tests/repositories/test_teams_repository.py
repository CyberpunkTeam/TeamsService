import mongomock

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
