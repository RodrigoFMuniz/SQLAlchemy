import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session
from pathlib import Path
from typing import Optional
from sqlalchemy.future.engine import Engine

from models.model_base import ModelBase

__engine: Optional[Engine] = None

def create_engine(sqlite: bool = True):
  global __engine
  if __engine:
    return
  if sqlite:
    arquivo_db = 'db/picole.sqlite'
    folder = Path(arquivo_db).parent
    folder.mkdir(parents=True,exist_ok=True)
    conn_str = f'sqlite:///{arquivo_db}'
    __engine = sa.create_engine(url=conn_str,echo=False,connect_args ={"check_same_thread":False})
  else:
    conn_str = 'postgresql:///user:password@localhost:5432/picoles'