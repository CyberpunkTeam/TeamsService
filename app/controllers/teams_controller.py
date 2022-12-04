from fastapi import HTTPException
from app.models.teams import Teams


class TeamsController:
    @staticmethod
    def post(repository, team: Teams):
        team.tid = Teams.get_tid()
        ok = repository.insert(team)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return team

    @staticmethod
    def get(repository, tid=None, uid=None, top=False):
        result = repository.get(tid=tid, uid=uid)
        if len(result) == 0 and tid is not None:
            raise HTTPException(status_code=404, detail="Item not found")

        if top:
            return result[0]
        return result
