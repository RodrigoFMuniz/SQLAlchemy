from configs.base import BASE
from sqlalchemy import Column, String, Integer

class Filme(BASE):
    __tablename__ = "filmes"

    id:int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(80), nullable=False, unique=True)
    genero: str = Column(String(80), nullable=False)
    ano: int = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Filme {self.id} -> Título: {self.nome} - Ano {self.ano}'
