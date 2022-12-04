import uuid

from json import loads
from typing import List, Optional
from pydantic import BaseModel


class Teams(BaseModel):
    tid: Optional[str] = None
    name: str
    technologies: List[str]
    project_preferences: List[str]
    owner: str

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {
            "name": str,
            "tid": str,
            "technologies": list,
            "project_preferences": list,
            "owner": str,
        }

    @staticmethod
    def get_tid():

        myuuid = uuid.uuid4()
        return str(myuuid)
