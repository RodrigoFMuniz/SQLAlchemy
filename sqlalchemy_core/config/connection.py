from importlib.metadata import metadata
from sqlalchemy import Column, create_engine, MetaData, Integer, String, Numeric, ForeignKey, Table
from pathlib import Path
from datetime import datetime

from sqlalchemy.dialects.sqlite import JSON

metadata = MetaData()

db_name = f"db/cookies.sqlite"

_path = Path(db_name).parent
_path.mkdir(parents=True,exist_ok=True)

conn_str = f"sqlite:///{db_name}"


engine = create_engine(url=conn_str, echo=True)

connection = engine.connect()

# teste de inserção de uma tabela


cookie = Table('cookies', metadata, 
    Column('cookie_id', Integer(), primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(255)),
    Column('cookie_sku', String(55)),
    Column('quantity', Integer()),
    Column('unit_cost', Numeric(12,2))
)