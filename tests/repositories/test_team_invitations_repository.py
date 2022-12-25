import mongomock

from app import config
from app.models.team_invitations import TeamInvitations
from app.repositories.team_invitations_repository import TeamInvitationsRepository


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_save_team_invitation():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = TeamInvitationsRepository(url, db_name)
    tiid = "1"
    tid = "111"
    team_owner_uid = "1234"
    postulant_uid = "4444"
    created_date = "12-02-2022"
    updated_date = "14-04-2022"
    state = "PENDING"
    team_invitation = TeamInvitations(
        tiid=tiid,
        tid=tid,
        team_owner_uid=team_owner_uid,
        postulant_uid=postulant_uid,
        created_date=created_date,
        updated_date=updated_date,
        state=state,
    )

    ok = repository.insert(team_invitation)

    assert ok


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_team_invitation():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = TeamInvitationsRepository(url, db_name)

    tiid = "1"
    tid = "111"
    team_owner_uid = "1234"
    postulant_uid = "4444"
    created_date = "12-02-2022"
    updated_date = "14-04-2022"
    state = "PENDING"
    team_invitation = TeamInvitations(
        tid=tid,
        tiid=tiid,
        team_owner_uid=team_owner_uid,
        postulant_uid=postulant_uid,
        created_date=created_date,
        updated_date=updated_date,
        state=state,
    )

    ok = repository.insert(team_invitation)

    assert ok

    teams_found = repository.get()

    assert len(teams_found) == 1

    teams_found = repository.get(tid=tid)
    assert len(teams_found) == 1

    teams_found = repository.get(team_owner_uid=team_owner_uid)
    assert len(teams_found) == 1

    teams_found = repository.get(postulant_uid=postulant_uid)
    assert len(teams_found) == 1

    teams_found = repository.get(tiid=tiid)
    assert len(teams_found) == 1
