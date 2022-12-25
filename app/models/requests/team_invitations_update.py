from datetime import datetime
from json import loads
from typing import Optional
from pydantic import BaseModel


class TeamInvitationsUpdate(BaseModel):
    tiid: Optional[str]
    state: str
    updated_date: Optional[str]

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    def complete(self, tiid):
        self.tiid = tiid
        local = datetime.now()
        self.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
