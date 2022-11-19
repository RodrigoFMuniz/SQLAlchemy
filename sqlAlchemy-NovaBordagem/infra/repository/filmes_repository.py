from configs.connection import DBConnectionHandler
from entities.filmes import Filme
from typing import Any

class FilmeRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filme).all()
            # data = db.get_engine().execute("Select * from filmes").all()
            return data
    
    def create(self, filme: Filme):
        with DBConnectionHandler() as db:
            data = db.session.add(filme)
            print(f"Create: {data}")
            db.session.commit()
    
    def update(self, criteria: Any, coluna, val_atualizado):
        with DBConnectionHandler() as db:
            if isinstance(criteria,int):
                data = db.session.query(Filme).filter(Filme.id == criteria).update({coluna: val_atualizado})
            elif criteria == "all":
                data = db.session.query(Filme).update({coluna: val_atualizado})
                print(f"Update: {data}")
            db.session.commit()
    
    def delete(self, filme_id:int):
        with DBConnectionHandler() as db:
            data = db.session.query(Filme).filter(Filme.id == filme_id).delete()
            print(f"Delete: {data}")
            db.session.commit()
    
        