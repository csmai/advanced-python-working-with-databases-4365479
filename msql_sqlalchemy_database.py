import sqlalchemy
import os
from sqlalchemy.orm import registry

password = os.getenv("P4PASSWD")

engine_string = f"mysql+mysqlconnector://root:{password}@localhost/projects"
engine = sqlalchemy.create_engine(engine_string, echo=True)

mapper_registry = registry()
Base = mapper_registry.generate_base()
# mapper_registry.metadata


class Projects(Base):
    __tablename__ = "projects"
    project_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(length=50))
    description = sqlalchemy.Column(sqlalchemy.String(length=100))

    def __repr__(self) -> str:
        return f"Project(title={self.title}, description={self.description})"


class Tasks(Base):
    __tablename__ = "Tasks"
    task_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    description = sqlalchemy.Column(sqlalchemy.String(50))
    project_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey("projects.project_id")
    )

    project = sqlalchemy.orm.relationship("Projects")

    def __repr__(self) -> str:
        return f"Task(description={self.description})"
    

