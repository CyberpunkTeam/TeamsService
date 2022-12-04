from cpunk_mongo.db import DataBase

from app.models.teams import Teams


class TeamsRepository(DataBase):
    COLLECTION_NAME = "teams"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, tid=None, uid=None):
        if tid is None and uid is None:
            return self.filter(self.COLLECTION_NAME, {}, output_model=Teams)
        elif uid is not None:
            return self.find_by(self.COLLECTION_NAME, "owner", uid, output_model=Teams)
        else:
            return self.find_by(self.COLLECTION_NAME, "tid", tid, output_model=Teams)

    def insert(self, team: Teams):
        return self.save(self.COLLECTION_NAME, team)

    @staticmethod
    def create_repository(url, database_name):
        return TeamsRepository(url, database_name)
