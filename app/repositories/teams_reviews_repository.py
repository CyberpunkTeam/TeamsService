from cpunk_mongo.db import DataBase

from app.models.teams_reviews import TeamsReviews


class TeamsReviewsRepository(DataBase):
    COLLECTION_NAME = "teams_reviews"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, tid=None, pid=None):
        filters = {}
        if tid is not None:
            filters["tid"] = tid
        if pid is not None:
            filters["pid"] = pid

        return self.filter(self.COLLECTION_NAME, filters, output_model=TeamsReviews)

    def insert(self, team_review: TeamsReviews):
        return self.save(self.COLLECTION_NAME, team_review)

    @staticmethod
    def create_repository(url, database_name):
        return TeamsReviewsRepository(url, database_name)

    def reset(self):
        return self.delete_all(self.COLLECTION_NAME)
