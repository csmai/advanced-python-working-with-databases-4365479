from sqlalchemy import create_engine, text, Column, Integer, String, Numeric, select
from sqlalchemy.orm import Session, registry
import os


def create_database(engine):
    # Create the database if it doesn't exist
    with engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))


def create_sales_table(engine):
    with engine.connect() as connection:
        connection.execute(text(f"USE {db_name}"))
        connection.execute(
            text(
                """
            CREATE TABLE IF NOT EXISTS sales (
                order_num INT PRIMARY KEY,
                order_type VARCHAR(50),
                cust_name VARCHAR(50),
                prod_number VARCHAR(50),
                prod_name VARCHAR(50),
                quantity INT,
                price DECIMAL(10, 2),
                discount DECIMAL(10, 2),
                order_total DECIMAL(10, 2)
            )
        """
            )
        )


if __name__ == "__main__":
    db_name = "Red30"
    password = os.getenv("P4PASSWD")
    database_conn_str = f"mysql+mysqlconnector://root:{password}@localhost"

    db_creator_engine = create_engine(database_conn_str, echo=True)
    create_database(db_creator_engine)

    engine = create_engine(database_conn_str + f"/{db_name}", echo=True)
    mapper_registry = registry()
    Base = mapper_registry.generate_base()
    Base.metadata.create_all(engine)
    create_sales_table(engine)

    class Sales(Base):
        __tablename__ = "sales"
        order_num = Column(Integer, primary_key=True)
        order_type = Column(String)
        cust_name = Column(String)
        prod_number = Column(String)
        prod_name = Column(String)
        quantity = Column(Integer)
        price = Column(Numeric)
        discount = Column(Numeric)
        order_total = Column(Numeric)

    sales_data = [
        Sales(
            order_num=1,
            order_type="Type1",
            cust_name="Customer1",
            prod_number="P1",
            prod_name="Product1",
            quantity=10,
            price=9.99,
            discount=0.1,
            order_total=89.91,
        ),
        Sales(
            order_num=2,
            order_type="Type2",
            cust_name="Customer2",
            prod_number="P2",
            prod_name="Product2",
            quantity=5,
            price=19.99,
            discount=0.05,
            order_total=94.95,
        ),
        Sales(
            order_num=3,
            order_type="Type3",
            cust_name="Customer3",
            prod_number="P3",
            prod_name="Product3",
            quantity=3,
            price=12.99,
            discount=0.15,
            order_total=33.22,
        ),
        Sales(
            order_num=4,
            order_type="Type4",
            cust_name="Customer4",
            prod_number="P4",
            prod_name="Product4",
            quantity=8,
            price=7.99,
            discount=0.2,
            order_total=55.92,
        ),
        Sales(
            order_num=5,
            order_type="Type5",
            cust_name="Customer5",
            prod_number="P5",
            prod_name="Product5",
            quantity=2,
            price=24.99,
            discount=0.1,
            order_total=44.98,
        ),
    ]
    # with Session(engine) as session:
    #     # Create 5 instances of sales and add them to the session

    #     session.bulk_save_objects(sales_data)
    #     session.commit()

    with Session(engine) as session:
        for row in result:
            print(row)
