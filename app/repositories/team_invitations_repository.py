from cpunk_mongo.db import DataBase

from app.models.requests.team_invitations_update import TeamInvitationsUpdate
from app.models.team_invitations import TeamInvitations


class TeamInvitationsRepository(DataBase):
    COLLECTION_NAME = "team_invitations"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(
        self, tid=None, team_owner_uid=None, postulant_uid=None, tiid=None, state=None
    ):
        params = {}

        if state is not None:
            params["state"] = state

        if tid is not None:
            params["tid"] = tid
        if team_owner_uid is not None:
            params["team_owner_uid"] = team_owner_uid

        if postulant_uid is not None:
            params["postulant_uid"] = postulant_uid

        if tiid is not None:
            params["tiid"] = tiid

        return self.filter(self.COLLECTION_NAME, params, output_model=TeamInvitations)

    def insert(self, team: TeamInvitations):
        return self.save(self.COLLECTION_NAME, team)

    def update_team(self, team: TeamInvitationsUpdate):
        ok = self.update(self.COLLECTION_NAME, "tiid", team.tiid, team)
        return ok

    def reset(self):
        return self.delete_all(self.COLLECTION_NAME)
