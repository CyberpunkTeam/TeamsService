from app.models.teams import Teams
from app.models.technologies import Technologies


def test_create_team():
    team = Teams(
        name="GreenTeam",
        tid="4211",
        technologies=Technologies(programming_language=["Python", "React"]),
        project_preferences=["web", "AI", "Crypto"],
        owner="1234",
    )
    assert team.name == "GreenTeam"
    assert team.tid == "4211"
    assert team.technologies.programming_language == ["Python", "React"]
    assert team.project_preferences == ["web", "AI", "Crypto"]
