from datetime import datetime
from json import loads
from typing import Optional, List

import uuid
from pydantic.main import BaseModel

from app.models.position_states import PositionStates
from app.models.requirements import Requirements
from app.models.teams import Teams


class TeamsPositions(BaseModel):
    tpid: Optional[str]
    title: str
    description: str
    tid: str
    candidates: Optional[List[str]]
    created_date: Optional[str] = ""
    updated_date: Optional[str] = ""
    state: PositionStates = None
    team: Optional[Teams]
    requirements: Optional[Requirements]

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {
            "tpid": str,
            "title": str,
            "description": str,
            "tid": str,
            "candidates": list,
            "created_date": str,
            "updated_date": str,
            "state": str,
            "requirements": dict,
        }

    def complete(self):
        self.tpid = TeamsPositions.get_id()
        local = datetime.now()
        created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        self.created_date = created_date
        self.updated_date = created_date
        self.state = PositionStates.OPEN
        self.candidates = []

    @staticmethod
    def get_id():
        myuuid = uuid.uuid4()
        return str(myuuid)
