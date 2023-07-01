import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///users.db", echo=True)

metadata = sqlalchemy.MetaData()

table_object = sqlalchemy.Table(
    "Users",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
)

metadata.create_all(engine)
datalist = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
    },
    {
        "first_name": "Krist",
        "last_name": "Stew",
        "email": "kristen@gmail.com",
    },
    {
        "first_name": "Hey",
        "last_name": "Jude",
        "email": "beatles@example.com",
    },
    {
        "first_name": "Sue",
        "last_name": "Me",
        "email": "southpark@gmail.com",
    },
    {
        "first_name": "Wrong",
        "last_name": "Address",
        "email": "haha@example.com",
    },
]


with engine.connect() as conn:
    # Add datalist to table
    conn.execute(table_object.insert().values(datalist))

    # Define selection of the e-amils
    select_email_query = sqlalchemy.select(table_object.c.email)
    selection = conn.execute(select_email_query)
    for row in selection:
        print(row)

    # Print out everything
    for row in conn.execute(table_object.select()):
        print(row)
