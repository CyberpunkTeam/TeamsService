from app.models.team_invitations import TeamInvitations


def test_create_invitation():
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

    assert team_invitation.tiid == tiid
    assert team_invitation.tid == tid
    assert team_invitation.team_owner_uid == team_owner_uid
    assert team_invitation.postulant_uid == postulant_uid
    assert team_invitation.created_date == created_date
    assert team_invitation.updated_date == updated_date
    assert team_invitation.state == state
