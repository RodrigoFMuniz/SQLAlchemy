import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session
from pathlib import Path
from typing import Optional
from sqlalchemy.future.engine import Engine

from models.model_base import ModelBase

__engine: Optional[Engine] = None


'''Função para configuração a conexão com o banco de dados''' 
def create_engine(sqlite: bool = False) -> Engine:
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
    __engine = sa.create_engine(url=conn_str,echo=False)
  
  return __engine

'''Cria a sessão do banco de dados, inicializando a engine'''
def create_session() -> Session:
  global __engine
  if not __engine:
    create_engine(sqlite=True) #True pq estamos usando sqlite
  
  __session = sessionmaker(__engine,expire_on_commit=False,class_= Session)

  session: Session = __session()

  return session



  