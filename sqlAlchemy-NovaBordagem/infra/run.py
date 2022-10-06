from repository.filmes_repository import FilmeRepository

repo = FilmeRepository()
data = repo.select()
print(data)