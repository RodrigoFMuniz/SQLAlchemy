# SQLAlchemy

## Arquitetura

- DB API - Baseada no PEP 249 do Python
- SQLAlchemy Core
  - Schema / Types
  - SQL Expression Language
  - Engine
  - Connection Pooling
  - Dialect
- SQLAlchemy ORM

## Estrutura de um projeto

### db_session

- import sqlalchemy as sa
  - sqlachemy em si
- from sqlalchemy.orm import sessionmaker, Session
  - sessionmaker : Utlizado para criar uma sessão no SQLAlchemy
  - Session: utilizados para criar instâncias deste tipo.
- from pathlib import Path
  - Utilizado para criar diretório e arquivo
- from typing import Optional
  - Tipagem de dados opcionais
- from sqlalchemy.future.engine import Engine
  - Engine: utilizados para criar instâncias deste tipo.

from model_base import ModelBase
