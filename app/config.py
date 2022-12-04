# ENV VARS, CONSTANTS
import os

DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

DATABASE_URL = os.environ.get("DATABASE_URL", "server.example.com")
if DATABASE_USER is not None and DATABASE_PASSWORD is not None:
    DATABASE_URL = f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}@findmyteam.slcsp0t.mongodb.net/?retryWrites=true&w=majority"


DATABASE_NAME = os.environ.get("DATABASE_NAME", "test")
