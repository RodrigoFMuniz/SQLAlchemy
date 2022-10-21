from sqlalchemy import create_engine
from pathlib import Path

db_name = f"db/cookies.sqlite"
_path = Path(db_name).parent
# print(Path(conn_str).absolute())
_path.mkdir(parents=True,exist_ok=True)
conn_str = f"sqlite:///{db_name}"
engine = create_engine(url=conn_str, echo=True)

connection = engine.connect()