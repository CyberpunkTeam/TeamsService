from json import loads
from typing import List, Optional
from pydantic import BaseModel

from app.models.position_states import PositionStates


class TeamPositionUpdate(BaseModel):
    tpid: Optional[str]
    state: Optional[PositionStates]
    title: Optional[str]
    description: Optional[str]
    updated_date: Optional[str]

    def to_json(self):
        return loads(self.json(exclude_defaults=True))
