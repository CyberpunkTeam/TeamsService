from fastapi import HTTPException

from app.models.teams_reviews import TeamsReviews


class TeamsReviewsController:
    @staticmethod
    def post(repository, team_review: TeamsReviews):
        team_review.complete()
        ok = repository.insert(team_review)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")

        return team_review

    @staticmethod
    def get(repository, pid=None, tid=None):
        result = repository.get(pid=pid, tid=tid)
        return result
