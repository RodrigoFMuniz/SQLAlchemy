from email.policy import default
from enum import unique
import sqlalchemy as sa
from configs.base import BASE

class Ator(BASE):
    __tablename__ = "atores"

    id: int = sa.Column(sa.Integer, primary_key=True)
    nome:str = sa.Column(sa.String(45),nullable=False)
    sobrenome = sa.Column(sa.String(80), nullable=False)
    idade:int = sa.Column(sa.Integer, default=0,nullable=True)

    def __repr__(self)->str:
        return f"Nome: {self.nome} {self.sobrenome}\nIdade: {self.idade}"