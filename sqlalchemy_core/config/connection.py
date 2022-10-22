from sqlalchemy import create_engine
from pathlib import Path
from models import *

db_name = f"db/cookies.sqlite"

_path = Path(db_name).parent
_path.mkdir(parents=True,exist_ok=True)

conn_str = f"sqlite:///{db_name}"


engine = create_engine(url=conn_str, echo=True)

connection = engine.connect()


