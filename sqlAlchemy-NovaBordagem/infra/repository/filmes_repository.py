from configs.connection import DBConnectionHandler
from entities.filmes import Filme

class FilmeRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filme).all()
            # data = db.get_engine().execute("Select * from filmes").all()
            return data
    
    def create(self, filme: Filme):
        with DBConnectionHandler() as db:
            db.session.add(filme)
            db.session.commit()
    
    def update(self, filme_id: int):
        with DBConnectionHandler() as db:
            db.session.query(Filme).filter(Filme.id == filme_id).update({"ano":2020})
            db.session.commit()
    
    def delete(self, filme_id:int):
        with DBConnectionHandler() as db:
            db.session.query(Filme).filter(Filme.id == filme_id).delete()
            db.session.commit()
    
        