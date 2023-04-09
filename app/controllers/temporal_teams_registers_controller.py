from fastapi import HTTPException
from app.models.temporal_teams_registers import TemporalTeamsRegisters


class TemporalTeamsRegistersController:
    @staticmethod
    def post(repository, temporal_team_register: TemporalTeamsRegisters):
        ok = repository.insert(temporal_team_register)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")

        return temporal_team_register

    @staticmethod
    def get(repository, pid=None, tid=None):
        result = repository.get(pid=pid, tid=tid)
        return result
