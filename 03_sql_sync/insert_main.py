from conf.db_session import create_session

from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor

def insert_aditivo_nutritivo()->None:
    print("Cadastrando aditivo nutritivo")
    nome:str = input('Informe aditivo nutritivo:')
    formula_quimica: str = input("Informe a formula química: ")

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)

        session.commit()

    print('Aditivo nutritivo cadastrado com sucesso.')
    print(f"ID:{an.id}")
    print(f"Data de criação:{an.data_criacao}")
    print(f"Nome:{an.nome}")
    print(f"Formula química:{an.formula_quimica}")

def insert_sabor()->None:
    print("Cadastrando sabor")
    nome:str = input('Informe sabor:')

    sabor: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)

        session.commit()

    print('Sabor cadastrado com sucesso.')
    print(f"ID:{sabor.id}")
    print(f"Data de criação:{sabor.data_criacao}")
    print(f"Nome:{sabor.nome}")


if __name__ == "__main__":
    insert_aditivo_nutritivo()
    # insert_sabor()