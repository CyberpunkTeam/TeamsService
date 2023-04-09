from json import loads

from pydantic import BaseModel


class TemporalTeamsRegisters(BaseModel):
    pid: str
    tid: str

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {
            "pid": str,
            "tid": str,
        }
