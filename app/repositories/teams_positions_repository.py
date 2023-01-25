from cpunk_mongo.db import DataBase

from app.models.teams_positions import TeamsPositions
from app.models.teams_reviews import TeamsReviews


class TeamsPositionsRepository(DataBase):
    COLLECTION_NAME = "teams_positions"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, tid=None, tpid=None, state=None):
        filters = {}
        if tid is not None:
            filters["tid"] = tid
        if tpid is not None:
            filters["tpid"] = tpid
        if state is not None:
            filters["state"] = state

        return self.filter(self.COLLECTION_NAME, filters, output_model=TeamsPositions)

    def insert(self, team_position: TeamsPositions):
        return self.save(self.COLLECTION_NAME, team_position)

    @staticmethod
    def create_repository(url, database_name):
        return TeamsPositionsRepository(url, database_name)

    def reset(self):
        return self.delete_all(self.COLLECTION_NAME)

    def update_team(self, team_position: TeamsPositions):
        ok = self.update(
            self.COLLECTION_NAME, "tpid", team_position.tpid, team_position
        )
        return ok
