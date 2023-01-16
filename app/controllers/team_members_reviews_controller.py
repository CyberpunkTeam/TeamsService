from fastapi import HTTPException

from app.models.team_members_reviews import TeamMembersReviews


class TeamMembersReviewsController:
    @staticmethod
    def post(repository, team_member_review: TeamMembersReviews):
        team_member_review.complete()
        ok = repository.insert(team_member_review)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")

        return team_member_review

    @staticmethod
    def get(
        repository,
        pid=None,
        tid=None,
        member_reviewer: str = None,
        member_reviewed: str = None,
    ):
        result = repository.get(
            pid=pid,
            tid=tid,
            member_reviewer=member_reviewer,
            member_reviewed=member_reviewed,
        )
        return result
