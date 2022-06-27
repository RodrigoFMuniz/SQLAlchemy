from optparse import Option
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session
from pathlib import Path
from typing import Optional
from sqlalchemy.future.engine import Engine

from models.model_base import ModelBase

__engine: Optional[Engine] = None

def create_engine(sqlite:bool = True):
    global __engine

    if __engine:
        return
    if sqlite:
        arquivo_db = 'db/picoles.sqlite'