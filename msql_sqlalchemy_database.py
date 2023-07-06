import sqlalchemy
import os
from sqlalchemy.orm import registry, Session

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
        return f"Project(title={self.title}, description={self.description}, project_id={self.project_id})"


class Tasks(Base):
    __tablename__ = "tasks"
    task_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    description = sqlalchemy.Column(sqlalchemy.String(50))
    project_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey("projects.project_id")
    )

    project = sqlalchemy.orm.relationship("Projects")

    def __repr__(self) -> str:
        return f"Task(description={self.description})"


Base.metadata.create_all(engine)

with Session(engine) as session:
    organize_project = Projects(
        title="Organize Closet", description="Organize Closet by color and style"
    )

    session.add(organize_project)

    session.flush()

    tasks = [
        Tasks(
            description="Decide what to donate", project_id=organize_project.project_id
        ),
        Tasks(
            description="Organize winter clothes",
            project_id=organize_project.project_id,
        ),
        Tasks(
            description="Organize summer clothes",
            project_id=organize_project.project_id,
        ),
    ]
    session.bulk_save_objects(tasks)
    session.commit()


with Session(engine) as session:
    stm = sqlalchemy.select(Projects).where(Projects.title == "Organize Closet")
    org_closet_project = session.execute(stm).fetchone()
    print(org_closet_project)

    stm = sqlalchemy.select(Tasks).where(
        Tasks.project_id == org_closet_project[0].project_id
    )
    results = session.execute(stm).fetchall()
    for row in results:
        print(row[0])
