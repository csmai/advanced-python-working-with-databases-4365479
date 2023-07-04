import sqlalchemy
import os

password = os.getenv("P4PASSWD")

engine_string = f"mysql+mysqlconnector://root:{password}@localhost/projects"
engine = sqlalchemy.create_engine(engine_string, echo=True)
