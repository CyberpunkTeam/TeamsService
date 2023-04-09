from cpunk_mongo.db import DataBase

from app.models.temporal_teams_registers import TemporalTeamsRegisters


class TemporalTeamsRegistersRepository(DataBase):
    COLLECTION_NAME = "temporal_teams_registers"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, tid=None, pid=None):
        filters = {}

        if tid is not None:
            filters["tid"] = tid
        if pid is not None:
            filters["pid"] = pid

        return self.filter(
            self.COLLECTION_NAME, filters, output_model=TemporalTeamsRegisters
        )

    def insert(self, team: TemporalTeamsRegisters):
        return self.save(self.COLLECTION_NAME, team)
