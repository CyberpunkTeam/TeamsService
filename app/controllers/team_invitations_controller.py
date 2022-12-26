from fastapi import HTTPException

from app.models.requests.team_invitations_update import TeamInvitationsUpdate
from app.models.states import States
from app.models.team_invitations import TeamInvitations


class TeamInvitationsController:
    @staticmethod
    def post(repository, team_invitation: TeamInvitations):
        team_invitation.complete()
        ok = repository.insert(team_invitation)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return team_invitation

    @staticmethod
    def get(
        repository,
        tid=None,
        team_owner_uid=None,
        postulant_uid=None,
        tiid=None,
        state: States = None,
    ):
        result = repository.get(
            tid=tid,
            team_owner_uid=team_owner_uid,
            postulant_uid=postulant_uid,
            tiid=tiid,
            state=state,
        )

        if tiid is not None:
            return result[0]
        return result

    @staticmethod
    def update(repository, tiid, team_invitation: TeamInvitationsUpdate):
        team_invitation.complete(tiid)
        ok = repository.update_team(team_invitation)
        if not ok:
            raise HTTPException(
                status_code=500, detail="Error to update team invitation"
            )
        return TeamInvitationsController.get(repository, tiid=tiid)
