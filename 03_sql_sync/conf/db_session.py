'''
session maker: Cria a sessão
Session: Criar objetos usados na sessão
Path: Usado para criar diretório e arquivo na estrutura. Usado no sqlite3
typing: Tipagem de dados Opcionais, entre outros
Engine: Função para criar a sessão do DB, a conexão em si. Definir a forma de conexão e tipo de DB.
ModelBase: Usado para criar tabelas e campos
'''
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session # session maker: Cria a sessão / Session: Criar objetos usados na sessão
from pathlib import Path # Usado para criar diretório e arquivo na estrutura. Usado no sqlite3
from typing import Optional # Tipagem de dados Opcionais
from sqlalchemy.future.engine import Engine # Função para criar a sessão do DB, a conexão em si. Definir a forma de conexão e tipo de DB.

from models.model_base import ModelBase  # Usado para criar tabelas e campos

__engine: Optional[Engine] = None

'''
 .parent: Define que o diretório subirá um nível em relação ao atual
 mkdir : cria um diretório 
 parents: Respeita o local de criação do arquivo
 exist_ok: Se existir mantém, se não existir cria um novo arquivo.
 global: diz a função que a variável criada trata-se da variavel gloobal e não de escopo local.
 conn_str: Caminho da string de conexão
 sa.create_engine: Chama a função sqlalchemy para criação de engine
 url: caminho do DB
 echo: False
 connect_args: checagem de threads
'''

def create_engine(sqlite:bool = False):
  global __engine 
  if __engine:
    return
  if sqlite:
    arquivo_db = 'db/picoles.sqlite'
    folder = Path(arquivo_db).parent # Define que o diretório subirá um nível em relação ao atual
    folder.mkdir(parents=True,exist_ok=True) # mkdir : cria um diretório / parents: Respeita o local de criação do arquivo / exist_ok: Se existir mantém, se não existir cria um novo arquivo.
    conn_str = f'sqlite:///{arquivo_db}'
    __engine = sa.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread":False})
  else:
    conn_str = "postgreesql://user_postgre_db:password@localhost:port_db/bd_name"
    __engine = sa.create_engine(url=conn_str, echo=False)
  
  return __engine

