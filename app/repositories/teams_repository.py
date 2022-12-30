from cpunk_mongo.db import DataBase

from app.models.requests.team_update import TeamUpdate
from app.models.teams import Teams


class TeamsRepository(DataBase):
    COLLECTION_NAME = "teams"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, tid=None, uid=None, owner=None):
        if tid is None and uid is None:
            return self.filter(self.COLLECTION_NAME, {}, output_model=Teams)
        elif uid is not None:
            return self.list_teams_filter_in_by("members", [uid])
        elif creator is not None:
            return self.find_by(
                self.COLLECTION_NAME, "owner", owner, output_model=Teams
            )
        else:
            return self.find_by(self.COLLECTION_NAME, "tid", tid, output_model=Teams)

    def insert(self, team: Teams):
        return self.save(self.COLLECTION_NAME, team)

    def exists(self, team: Teams):
        result = self.find_by(
            self.COLLECTION_NAME, "name", team.name, output_model=Teams
        )
        return len(result) > 0

    def update_team(self, team: Teams):
        ok = self.update(self.COLLECTION_NAME, "tid", team.tid, team)
        return ok

    def list_teams_filter_in_by(self, name, values):
        value_parsed = {"$in": values}
        return self.find_by(
            self.COLLECTION_NAME, name, value_parsed, output_model=Teams
        )

    @staticmethod
    def create_repository(url, database_name):
        return TeamsRepository(url, database_name)

    def reset(self):
        return self.delete_all(self.COLLECTION_NAME)

    def put(self, team: TeamUpdate):
        return self.update(self.COLLECTION_NAME, "tid", team.tid, team)

    def search(self, fields, value):
        return self.ilike(self.COLLECTION_NAME, fields, value, output_model=Teams)
