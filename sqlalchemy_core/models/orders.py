from importlib.metadata import metadata
from sqlalchemy import Column, MetaData, Table, ForeignKey, Integer

metadata = MetaData()

orders = Table(
    'orders', 
    metadata,
    Column('order_id',Integer(), primary_key=True),
    Column('user_id',ForeignKey('users.user_id'))
)