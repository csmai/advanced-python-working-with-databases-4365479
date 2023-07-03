import mysql.connector as mysql
import os

# This code adds some additional data to the existing projects database


def connect(db_name, password):
    try:
        return mysql.connect(
            host="localhost", database=db_name, user="root", password=password
        )
    except mysql.Error as e:
        print(e)


def add_project(cursor, project_title, project_description, tasks):
    cursor.execute(
        "INSERT INTO projects VALUES(%s, %s)", (project_title, project_description)
    )


if __name__ == "__main__":
    db = connect("projects", os.environ.get("P4PASSWD"))

    cursor = db.cursor()

    tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
    add_project(cursor, "Clean house", "Clean house by room", tasks)
    db.commit()

    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    print(project_records)

    cursor.execute("SELECT * FROM tasks")
    tasks_records = cursor.fetchall()
    print(tasks_records)
