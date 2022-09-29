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

## Estrutura model base
> Instacia um objeto Sql alchemy para ser usado no desenvolvimento do projeto

    from sqlalchemy.ext.declarative import declarative_base

    ModelBase = declarative_base()