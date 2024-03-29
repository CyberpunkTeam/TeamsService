from fastapi import HTTPException
from datetime import datetime
from app.models.requests.team_update import TeamUpdate
from app.models.team_states import TeamStates
from app.models.teams import Teams


class TeamsController:
    @staticmethod
    def post(repository, team: Teams):
        if repository.exists(team):
            raise HTTPException(status_code=400, detail="Team name is not available")
        team.tid = Teams.get_tid()
        if len(team.members) == 0:
            team.members = [team.owner]

        local = datetime.now()
        team.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        team.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        team.temporal = team.temporal if team.temporal else False
        team.state = TeamStates.ACTIVE
        ok = repository.insert(team)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return team

    @staticmethod
    def get(repository, tid=None, uid=None, owner=None, top=False, tids=None):
        if tids is not None:
            return repository.get_by_list(tids)

        result = repository.get(tid=tid, uid=uid, owner=owner)
        if len(result) == 0 and tid is not None:
            raise HTTPException(status_code=404, detail="Team not found")

        if top:
            return result[0]
        return result

    @staticmethod
    def search(repository, search):
        fields = ["name"]
        return repository.search(fields, search)

    @staticmethod
    def update(repository, team: Teams):
        try:
            local = datetime.now()
            team.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
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
        local = datetime.now()
        team.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")

        return TeamsController.update(repository, team)

    @staticmethod
    def put(repository, tid, team: TeamUpdate):
        local = datetime.now()
        team.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")

        TeamsController.exists(repository, tid)
        team.tid = tid
        if repository.put(team):
            result = repository.get(tid=tid)
            return result[0]
        else:
            raise HTTPException(status_code=500, detail="Error to update team")

    @staticmethod
    def exists(repository, tid):
        result = repository.get(tid=tid)
        if len(result) == 0 and tid is not None:
            raise HTTPException(status_code=404, detail="Team not found")

    @staticmethod
    def get_metrics(repository):
        teams = repository.get()
        created_metrics = {}
        states_metrics = {}
        for team in teams:
            team_created_date = team.created_date[:10]
            created_metrics[team_created_date] = (
                created_metrics.get(team_created_date, 0) + 1
            )
            states_metrics[team.state] = states_metrics.get(team.state, 0) + 1

        payload = {
            "teams_created": {
                "labels": list(created_metrics.keys()),
                "values": list(created_metrics.values()),
            },
            "teams_state": {
                "labels": list(states_metrics.keys()),
                "values": list(states_metrics.values()),
            },
        }

        return payload
