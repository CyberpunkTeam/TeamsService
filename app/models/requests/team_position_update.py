from json import loads
from typing import Optional
from pydantic import BaseModel

from app.models.position_states import PositionStates
from app.models.requirements import Requirements


class TeamPositionUpdate(BaseModel):
    tpid: Optional[str]
    state: Optional[PositionStates]
    title: Optional[str]
    description: Optional[str]
    updated_date: Optional[str]
    requirements: Optional[Requirements]

    def to_json(self):
        return loads(self.json(exclude_defaults=True))
