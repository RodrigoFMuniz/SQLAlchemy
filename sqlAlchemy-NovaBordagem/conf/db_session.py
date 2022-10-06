# from sqlalchemy import Column, String, Integer
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from pathlib import Path
# from sqlalchemy.ext.declarative import declarative_base

# arquivo_db = 'db/cinema.sqlite'
# folder = Path(arquivo_db).parent
# folder.mkdir(parents=True,exist_ok=True)
# conn_str = f'sqlite:///{arquivo_db}'

# engine = create_engine(url=conn_str)

# BASE = declarative_base()
# session = sessionmaker(bind=engine)
# _session = session()



# # Entidades

# class Filme(BASE):
#     __tablename__ = "filmes"

#     id:int = Column(Integer, primary_key=True)
#     nome: str = Column(String(80), nullable=False)
#     genero: str = Column(String(80), nullable=False)
#     ano: int = Column(Integer, nullable=False)

#     def __repr__(self):
#         return f'Filme {self.id} -> Título: {self.nome} - Ano {self.ano}'


# # SQL

# # Create

# # filme2 = Filme(id=3,nome="ET", genero="Drama", ano=1993)

# # _session.add(filme2)
# # _session.commit()
# # _session.close()


# #Delete

# # _session.query(Filme).filter(Filme.id==3).delete()
# # _session.commit()
# # _session.close()

# # update

# # _session.query(Filme).filter(Filme.id>0).update({"genero": "Aventura"})
# # _session.commit()

# # Read
# data = _session.query(Filme).all()

# _session.close()

# # conn = engine.connect()
# # # print(conn)

# # query_string= f'''
# #     CREATE TABLE Filmes(
# #     id int NOT NULL,
# #     nome varchar(80) NOT NULL,
# #     genero int NOT NULL,
# #     ano int NOT NULL,
# #     PRIMARY KEY(id)
# # );
# # '''

# # query_insert= f'''
# #     INSERT INTO Filmes VALUES(1, 'Forrest Gump', 'Drama', 1994);
# # '''
# # query_select_all= f'''
# #     select * from filmes;
# # '''
# # query_select= f'''
# #     select * from filmes where id=1;
# # '''

# # response = conn.execute(query_string)

# # print(response.all())
# # conn.close()

# if __name__== "__main__":
#     print(data)
#     # for row in response:
#     #     print(row.id)
#     #     print(row.nome)
#     #     print(row.genero)
#     #     print(row.ano)
#     # print(__name__)
        
    
    
