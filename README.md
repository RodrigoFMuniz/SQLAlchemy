# SQLAlchemy

## Arquitetura

- DB API - Baseada no PEP 249 do Python
- SQLAlchemy Core
  - Schema / Types
  - SQL Expression Language
  - Engine
  - Connection Pooling
  - Dialect
- SQLAlchemy ORM - utilizada para sw com orientação a objetos

## Estrutura de um projeto

### Estrutura model_base

> Instacia um objeto Sql alchemy para ser usado no desenvolvimento do projeto

    from sqlalchemy.ext.declarative import declarative_base

    ModelBase = declarative_base()

### Estrutura db_session

> - create_engine() define a configuração de conexão do SQLAlchemy com o banco de dados
> - create_session() Cria a conexão com banco de dados em si
> - create_tables() Cria as tabelas no banco de dados

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

    def create_engine(sqlite:bool = False)-> Engine:
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

      '''
      session: cria uma sessão que usará a máquina configurada de db
      create_engine(sqlite=True): Cria uma máquina configurada para conexão sqlite de DB
      __engine: Variavel para armazenamento das configurações do banco de dados
      expire_on_commit=False: Não expira a cada commit, ou cada inserção no DB
      class_=Session: Classe usada para definir o modelo de classe para criar uma nova sessão/conexão
      '''

    def create_session()-> Session:
      global __engine
      if not __engine:
        create_engine(sqlite=True)
      __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

      session: Session = __session
      return session


    '''
    Cria as tabelas no banco de dados
    '''

    def create_tables()->None:
      global __engine
      if not __engine:
        create_engine(sqlite=True)
      import models.__all_models
      ModelBase.metadata.drop_all(__engine)
      ModelBase.metadata.create_all(__engine)

### Estrutura create_main

> Inicia o banco de dados, baseado na estrura db_session

    from conf.db_session import create_tables

    if __name__ == "__main__":
      create_tables()

### Estrutura \_\_all_models

> - Local de importação de todos os models/schemas produzidos no DB
