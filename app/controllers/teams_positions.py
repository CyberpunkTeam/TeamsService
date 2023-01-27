from datetime import datetime

from fastapi import HTTPException

from app.models.requests.team_position_update import TeamPositionUpdate
from app.models.teams_positions import TeamsPositions


class TeamsPositionsController:
    @staticmethod
    def post(repository, teams_repository, team_position: TeamsPositions):
        team_position.complete()
        ok = repository.insert(team_position)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")

        team = teams_repository.get(tid=team_position.tid)
        team_position.team = team[0]

        return team_position

    @staticmethod
    def get(repository, team_repository, tid=None, state=None, tpid=None):
        result = repository.get(tid=tid, state=state, tpid=tpid)

        tids = [team_position.tid for team_position in result]
        if len(tids) > 0:
            teams = team_repository.get_by_list(tids)
            teams_hash = {team.tid: team for team in teams}
            for team_position in result:
                team_position.team = teams_hash.get(team_position.tid)

        if tpid is not None:
            return result[0]
        return result

    @staticmethod
    def add_candidate(repository, teams_repository, tpid=None, candidate_id=None):
        try:
            position = TeamsPositionsController.get(
                repository, teams_repository, tpid=tpid
            )
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
