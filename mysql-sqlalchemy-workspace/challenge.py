from sqlalchemy import (
    create_engine,
    text,
    Column,
    Integer,
    String,
    Numeric,
    select,
    desc,
)
from sqlalchemy.orm import Session, registry
import os


def create_database(engine):
    # Create the database if it doesn't exist
    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
        conn.execute(text(f"USE {db_name}"))


if __name__ == "__main__":
    db_name = "Red30_2"
    password = os.getenv("P4PASSWD")
    database_conn_str = f"mysql+mysqlconnector://root:{password}@localhost"

    db_creator_engine = create_engine(database_conn_str, echo=True)
    create_database(db_creator_engine)

    engine = create_engine(database_conn_str + f"/{db_name}", echo=True)

    mapper_registry = registry()
    Base = mapper_registry.generate_base()

    class Sales(Base):
        __tablename__ = "sales"
        order_num = Column(Integer, primary_key=True)
        order_type = Column(String(30))
        cust_name = Column(String(30))
        prod_number = Column(String(30))
        prod_name = Column(String(30))
        quantity = Column(Integer)
        price = Column(Numeric)
        discount = Column(Numeric)
        order_total = Column(Numeric)

    Base.metadata.create_all(engine)

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

    with Session(engine) as session:
        session.add_all(sales_data)

        query = select(Sales).order_by(desc(Sales.order_total))
        most_expensive_order = session.execute(query).fetchone()
        print(most_expensive_order[0].cust_name, most_expensive_order[0].order_total)

        most_expensive_order = session.execute(query).scalar()
        print(most_expensive_order.cust_name, most_expensive_order.order_total)
