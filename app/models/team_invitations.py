import uuid
from datetime import datetime

from json import loads
from typing import Optional
from pydantic import BaseModel

from app.models.teams import Teams


class TeamInvitations(BaseModel):
    tiid: Optional[str]
    tid: str
    team_owner_uid: str
    postulant_uid: str
    created_date: Optional[str]
    updated_date: Optional[str]
    state: Optional[str]
    metadata: Optional[dict]

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {
            "tiid": str,
            "tid": str,
            "team_owner_uid": str,
            "postulant_uid": str,
            "created_date": str,
            "updated_date": str,
            "state": str,
        }

    @staticmethod
    def get_tid():
        myuuid = uuid.uuid4()
        return str(myuuid)

    def complete(self):
        self.tiid = TeamInvitations.get_tid()
        local = datetime.now()
        self.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        self.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        self.state = "PENDING"
