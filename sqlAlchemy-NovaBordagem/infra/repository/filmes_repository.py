from configs.connection import DBConnectionHandler
from entities.filmes import Filme

class FilmeRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filme).all()
            return data