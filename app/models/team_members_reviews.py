from datetime import datetime
from json import loads
from typing import Optional

from pydantic.main import BaseModel


class TeamMembersReviews(BaseModel):
    pid: str
    tid: str
    member_reviewer: str
    member_reviewed: str
    rating: int
    created_date: Optional[str] = ""

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {
            "pid": str,
            "tid": str,
            "member_reviewer": str,
            "member_reviewed": str,
            "created_date": str,
            "rating": int,
        }

    def complete(self):
        local = datetime.now()
        created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        self.created_date = created_date
