from fastapi import HTTPException
from app.models.teams import Teams


class TeamsController:
    @staticmethod
    def post(repository, team: Teams):
        if repository.exists(team):
            raise HTTPException(status_code=400, detail="Team name is not available")
        team.tid = Teams.get_tid()
        team.members = [team.owner]
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

    @staticmethod
    def update(repository, team: Teams):
        try:
            ok = repository.update_team(team)
            if not ok:
                raise HTTPException(status_code=500, detail="Error to update team")
            return {"message": "Team updated"}
        except:
            raise HTTPException(status_code=500, detail="Error to update team")

    @staticmethod
    def add_member(repository, tid, new_member):
        team = TeamsController.get(repository, tid, top=True)

        if new_member in team.members:
            raise HTTPException(status_code=400, detail="Member is already in team")

        team.members.append(new_member)

        return TeamsController.update(repository, team)
