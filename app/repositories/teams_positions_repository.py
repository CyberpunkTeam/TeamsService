from cpunk_mongo.db import DataBase

from app.models.requests.team_position_update import TeamPositionUpdate
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

    def get(
        self,
        tid=None,
        tpid=None,
        state=None,
        programming_languages=None,
        frameworks=None,
        platforms=None,
        databases=None,
    ):
        filters = {}
        if tid is not None:
            filters["tid"] = tid
        if tpid is not None:
            filters["tpid"] = tpid
        if state is not None:
            filters["state"] = state

        if programming_languages is not None and len(programming_languages) > 0:
            filters["requirements.programming_language"] = {
                "$in": programming_languages
            }

        if frameworks is not None and len(frameworks) > 0:
            filters["requirements.frameworks"] = {"$in": frameworks}

        if platforms is not None and len(platforms) > 0:
            filters["requirements.platforms"] = {"$in": platforms}

        if databases is not None and len(databases) > 0:
            filters["requirements.databases"] = {"$in": databases}

        return self.filter(self.COLLECTION_NAME, filters, output_model=TeamsPositions)

    def insert(self, team_position: TeamsPositions):
        return self.save(self.COLLECTION_NAME, team_position)

    @staticmethod
    def create_repository(url, database_name):
        return TeamsPositionsRepository(url, database_name)

    def reset(self):
        return self.delete_all(self.COLLECTION_NAME)

    def update_position_team(self, team_position: TeamsPositions):
        ok = self.update(
            self.COLLECTION_NAME, "tpid", team_position.tpid, team_position
        )
        return ok

    def put(self, team_position: TeamPositionUpdate):
        return self.update(
            self.COLLECTION_NAME, "tpid", team_position.tpid, team_position
        )
