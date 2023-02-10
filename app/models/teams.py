import uuid

from json import loads
from typing import List, Optional
from pydantic import BaseModel

from app.models.technologies import Technologies


class Teams(BaseModel):
    tid: Optional[str] = None
    name: str
    project_preferences: List[str]
    owner: str
    members: Optional[List[str]] = []
    created_date: Optional[str]
    updated_date: Optional[str]
    idioms: Optional[List[str]]
    technologies: Optional[Technologies]
    methodologies: Optional[List[str]]

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {
            "name": str,
            "tid": str,
            "project_preferences": list,
            "owner": str,
            "members": list,
            "created_date": str,
            "updated_date": str,
            "idioms": list,
            "technologies": dict,
            "methodologies": list,
        }

    @staticmethod
    def get_tid():
        myuuid = uuid.uuid4()
        return str(myuuid)

    def get_id(self):
        return self.tid
