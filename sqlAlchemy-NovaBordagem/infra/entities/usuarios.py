from unicodedata import name
import sqlalchemy as sa
from configs.base import BASE

class User(BASE):
    __tablename__ = "users"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(50), nullable=False)
    surname: str = sa.Column(sa.String(50), nullable=False)
    cpf: str = sa.Column(sa.String(11), nullable=False, unique=True)
    password: str = sa.Column(sa.String(256), nullable=False)

    def __repr__(self)->str:
        return f"""Nome: {self.name}\nSurname: {self.surname}\nCPF: {self.cpf}"""
