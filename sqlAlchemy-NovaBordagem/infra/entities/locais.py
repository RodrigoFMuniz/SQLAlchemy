import sqlalchemy as sa
from configs.base import BASE

class Local(BASE):
    __tablename__ = "locais"

    id: int = sa.Column(sa.Integer, primary_key=True)
    nome: str = sa.Column(sa.String(100), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Nome: {self.nome}"