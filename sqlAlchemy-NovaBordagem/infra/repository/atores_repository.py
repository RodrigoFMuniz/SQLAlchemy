from configs.connection import DBConnectionHandler
from entities.atores import Ator

class AtorRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Ator).all()
            # data = db.get_engine().execute("Select * from filmes").all()
            return data
    
    def random_query(self, query_string: str)->None:
        with DBConnectionHandler() as db:
            data = db.get_engine()
            data.execute(query_string)
    
    def init_tables(self):
        with DBConnectionHandler() as db:
            db.create_table()
    

            

# # query_string= f'''
# #     CREATE TABLE Filmes(
# #     id int NOT NULL,
# #     nome varchar(80) NOT NULL,
# #     genero int NOT NULL,
# #     ano int NOT NULL,
# #     PRIMARY KEY(id)
# # );



