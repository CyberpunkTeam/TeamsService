from app.models.teams import Teams


def test_create_team():
    team = Teams(
        name="GreenTeam",
        tid="4211",
        technologies=["Python", "React"],
        project_preferences=["web", "AI", "Crypto"],
        owner="1234",
    )
    assert team.name == "GreenTeam"
    assert team.tid == "4211"
    assert team.technologies == ["Python", "React"]
    assert team.project_preferences == ["web", "AI", "Crypto"]
