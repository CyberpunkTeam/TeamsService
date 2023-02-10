from json import loads
from typing import List, Optional
from pydantic import BaseModel

from app.models.technologies import Technologies


class TeamUpdate(BaseModel):
    tid: Optional[str] = ""
    name: Optional[str] = ""
    project_preferences: Optional[List[str]]
    created_date: Optional[str]
    updated_date: Optional[str]
    idioms: Optional[List[str]]
    technologies: Optional[Technologies]
    methodologies: Optional[List[str]]

    def to_json(self):
        return loads(self.json(exclude_defaults=True))
