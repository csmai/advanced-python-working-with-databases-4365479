import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///movies.db", echo=True)

metadata = sqlalchemy.MetaData()

table_object = sqlalchemy.Table(
    "Movies",
    metadata,
    sqlalchemy.Column("title", sqlalchemy.Text),
    sqlalchemy.Column("director", sqlalchemy.Text),
    sqlalchemy.Column("year", sqlalchemy.Integer),
)

# Instantiate all the Tables in the database
metadata.create_all(engine)

# Connect to the database
with engine.connect() as conn:
    for row in conn.execute(sqlalchemy.select(table_object)):
        print(row)
