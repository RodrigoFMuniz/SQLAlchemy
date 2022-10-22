from importlib.metadata import metadata
from sqlalchemy import MetaData, Column, Integer, String, Numeric, Table, ForeignKey, DateTime
from config.connection import engine
# from models import cookies, users, orders, line_itens
import models as md

metadata = MetaData()

# cookies =  Table('cookies', metadata, 
#         Column('cookie_id', Integer(), primary_key=True),
#         Column('cookie_name', String(50), index=True),
#         Column('cookie_recipe_url', String(255)),
#         Column('cookie_sku', String(55)),
#         Column('quantity', Integer()),
#         Column('unit_cost', Numeric(12,2))
#     )
# users = Table('users', metadata,
#         Column('user_id', Integer(), primary_key=True),
#         Column('username', String(15), unique=True, nullable=True),
#         Column('email_address', String(255), unique=True, nullable=False),
#         Column('phone', String(20),nullable=False),
#         Column('password', String(25), nullable=False),
#         Column('created_on', DateTime(), default=datetime.now ,nullable=False),
#         Column('updated_on', DateTime(), default=datetime.now ,onupdate=datetime.now)
#     )

# line_itens = Table('line_itens', metadata,
#     Column('line_itens_id', Integer(), primary_key=True),
#     Column('orders_id', ForeignKey('orders.orders_id')),
#     Column('cookies_id',ForeignKey('cookies.cookies_id')),
#     Column('quantity', Integer()),
#     Column('extended_cost', Numeric(12,2))
# )
# orders = Table('orders', metadata,
#     Column('order_id',Integer(), primary_key=True),
#     Column('user_id',ForeignKey('users.user_id'))
# )

def create_tables():
    metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()