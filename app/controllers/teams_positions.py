from fastapi import HTTPException

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
    def get(repository, tid=None, state=None, tpid=None):
        result = repository.get(tid=tid, state=state, tpid=tpid)
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
