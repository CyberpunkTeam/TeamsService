from cpunk_mongo.db import DataBase

from app.models.team_members_reviews import TeamMembersReviews


class TeamMembersReviewsRepository(DataBase):
    COLLECTION_NAME = "team_members_reviews"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(
        self,
        tid=None,
        pid=None,
        member_reviewer: str = None,
        member_reviewed: str = None,
    ):
        filters = {}
        if tid is not None:
            filters["tid"] = tid
        if pid is not None:
            filters["pid"] = pid
        if member_reviewer is not None:
            filters["member_reviewer"] = member_reviewer
        if member_reviewed is not None:
            filters["member_reviewed"] = member_reviewed

        return self.filter(
            self.COLLECTION_NAME, filters, output_model=TeamMembersReviews
        )

    def insert(self, member_review: TeamMembersReviews):
        return self.save(self.COLLECTION_NAME, member_review)

    @staticmethod
    def create_repository(url, database_name):
        return TeamMembersReviewsRepository(url, database_name)

    def reset(self):
        return self.delete_all(self.COLLECTION_NAME)
