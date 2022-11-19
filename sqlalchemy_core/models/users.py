from sqlalchemy import MetaData, Table, String, Integer, Column, DateTime
from datetime import datetime

metadata = MetaData()

users = Table(
        'users', 
        metadata,
        Column('user_id', Integer(), primary_key=True),
        Column('username', String(15), unique=True, nullable=True),
        Column('email_address', String(255), unique=True, nullable=False),
        Column('phone', String(20),nullable=False),
        Column('password', String(25), nullable=False),
        Column('created_on', DateTime(), default=datetime.now ,nullable=False),
        Column('updated_on', DateTime(), default=datetime.now ,onupdate=datetime.now)
    )
