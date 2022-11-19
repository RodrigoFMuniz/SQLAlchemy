from configs.connection import DBConnectionHandler
from entities.locais import Local

class LocalRepository:
    def select():
        with DBConnectionHandler() as db:
            data = db.session.query(Local).all()
            return data
    
    def init_tables(self):
        with DBConnectionHandler() as db:
            db.create_table()