# from repository.filmes_repository import FilmeRepository
# from repository.atores_repository import AtorRepository
from repository.locais_repository import LocalRepository
# from entities.filmes import Filme
# # from entities.atores import Ator
# repo = FilmeRepository()
repo_ator = LocalRepository()
# data = repo.select()
repo_ator.init_tables()
# query_string= f'''
#     CREATE TABLE atores(
#     id int NOT NULL,
#     nome varchar(45) NOT NULL,
#     sobrenome varchar(80) NOT NULL,
#     ano int NOT NULL,
#     PRIMARY KEY(id)
# );
# '''
# data_ator = repo_ator.random_query(query_string=query_string)
# print(data_ator)

# for d in data:
#     print(f"ID: {d.id}")
#     print(f"Título: {d.nome}")
#     print(f"Tipo: {d.genero}")
#     print(f"Ano: {d.ano}")
# print(data[0].nome)

# repo_2 = FilmeRepository()
# filme_1 = Filme(id=6,nome="Halloween", genero="Terror", ano=2022)

# repo.create(filme_1)

# repo.update(1,"genero","Drama")
# repo.delete(6)

# repo_3 = FilmeRepository()
# data_2 = repo.select()

# for d in data_2:
#     print(f"ID: {d.id}")
#     print(f"Título: {d.nome}")
#     print(f"Tipo: {d.genero}")
#     print(f"Ano: {d.ano}")