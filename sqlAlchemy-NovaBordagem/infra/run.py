from repository.filmes_repository import FilmeRepository
from entities.filmes import Filme
repo = FilmeRepository()
# data = repo.select()

# for d in data:
#     print(f"ID: {d.id}")
#     print(f"Título: {d.nome}")
#     print(f"Tipo: {d.genero}")
#     print(f"Ano: {d.ano}")
# print(data[0].nome)

# repo_2 = FilmeRepository()
# filme_1 = Filme(id=6,nome="Halloween", genero="Terror", ano=2022)

# repo.create(filme_1)

repo.update(4,"genero","Ação")
# repo.delete(6)

# repo_3 = FilmeRepository()
data_2 = repo.select()

for d in data_2:
    print(f"ID: {d.id}")
    print(f"Título: {d.nome}")
    print(f"Tipo: {d.genero}")
    print(f"Ano: {d.ano}")