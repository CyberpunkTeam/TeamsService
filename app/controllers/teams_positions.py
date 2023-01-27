from datetime import datetime

from fastapi import HTTPException

from app.models.requests.team_position_update import TeamPositionUpdate
from app.models.teams_positions import TeamsPositions


class TeamsPositionsController:
    @staticmethod
    def post(repository, team_position: TeamsPositions):
        team_position.complete()
        ok = repository.insert(team_position)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")

        return team_position

    @staticmethod
    def get(repository, team_repository, tid=None, state=None, tpid=None):
        result = repository.get(tid=tid, state=state, tpid=tpid)

        tids = [team_position.tid for team_position in result]
        if len(tids) > 0:
            teams = team_repository.get_by_list(tids)
            for i in range(len(result)):
                team_position = result[i]
                team = teams[i]
                team_position.team = team

        if tpid is not None:
            return result[0]
        return result

    @staticmethod
    def add_candidate(repository, tpid=None, candidate_id=None):
        try:
            position = TeamsPositionsController.get(repository, tpid=tpid)
            position.candidates.append(candidate_id)
            ok = repository.update(position)
            if not ok:
                raise HTTPException(status_code=500, detail="Error to update team")
            return position

        except:
            raise HTTPException(status_code=500, detail="Error to update team")

    @staticmethod
    def put(repository, tpid, team_position: TeamPositionUpdate):
        local = datetime.now()
        team_position.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")

        team_position.tpid = tpid
        if repository.put(team_position):
            result = repository.get(tpid=tpid)
            return result[0]
        else:
            raise HTTPException(status_code=500, detail="Error to update team position")
