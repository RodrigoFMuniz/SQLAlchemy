from pydoc import describe
from conf.db_session import create_session

from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.revendedor import Revendedor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.lote import Lote

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

def insert_conservante()->None:
    print("Cadastrando conservante")
    nome:str = input('Informe conservante:')
    descricao:str = input('Descreva o conservante:')

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(conservante)
        session.commit()
    
    print('Conservante cadastrado com sucesso.')
    print(f"ID:{conservante.id}")
    print(f"Data de criação:{conservante.data_criacao}")
    print(f"Nome:{conservante.nome}")
    print(f"Descrição:{conservante.descricao}")

def insert_ingrediente()->None:
    print("Cadastrando ingrediente")
    nome:str = input('Informe o ingrediente:')

    ingrediente: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingrediente)
        session.commit()
    
    print('Ingrediente cadastrado com sucesso.')
    print(f"ID:{ingrediente.id}")
    print(f"Data de criação:{ingrediente.data_criacao}")
    print(f"Nome:{ingrediente.nome}")
    
def insert_revendedor()->None:
    print("Cadastrando revendedor")
    cnpj:str = input('Informe o cnpj:')
    razao_social:str = input('Informe a razão social:')
    contato:str = input('Informe o contato:')

    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social,contato=contato)

    with create_session() as session:
        session.add(revendedor)
        session.commit()
    
    print('Revendedor cadastrado com sucesso.')
    print(f"ID:{revendedor.id}")
    print(f"Data de criação:{revendedor.data_criacao}")
    print(f"CNPJ:{revendedor.cnpj}")
    print(f"Razão social:{revendedor.razao_social}")
    print(f"Contato:{revendedor.contato}")

def insert_tipo_embalagem()->None:
    print("Cadastrando tipo de embalagem")
    nome:str = input('Informe o tipo:')

    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(tipo_embalagem)
        session.commit()
    
    print('Tipo de embalagem cadastrado com sucesso.')
    print(f"ID:{tipo_embalagem.id}")
    print(f"Data de criação:{tipo_embalagem.data_criacao}")
    print(f"Nome:{tipo_embalagem.nome}")

def insert_tipo_picole()->None:
    print("Cadastrando tipo de picolé")
    nome:str = input('Informe o tipo:')

    tipo_picole: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tipo_picole)
        session.commit()
    
    print('Tipo de embalagem cadastrado com sucesso.')
    print(f"ID:{tipo_picole.id}")
    print(f"Data de criação:{tipo_picole.data_criacao}")
    print(f"Nome:{tipo_picole.nome}")

def insert_lote()->Lote:
    print("Cadastrando lote")
    id_tipo_picole:int = int(input('Informe o tipo:'))
    qtd:int = int(input('Informe a qtd:'))

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, qtd=qtd)

    with create_session() as session:
        session.add(lote)
        session.commit()
    
    return lote
    
    # print('Tipo de embalagem cadastrado com sucesso.')
    # print(f"ID:{tipo_picole.id}")
    # print(f"Data de criação:{tipo_picole.data_criacao}")
    # print(f"Nome:{tipo_picole.nome}")

if __name__ == "__main__":
    # insert_aditivo_nutritivo()
    # insert_sabor()
    # insert_conservante()
    # insert_ingrediente()
    # insert_revendedor()
    # insert_tipo_embalagem()
    # insert_tipo_picole()
    lote = insert_lote()

    print(f"ID:{lote.id}")
    print(f"Data de criação:{lote.data_criacao}")
    print(f"Tipo:{lote.id_tipo_picole}")
    print(f"Qtd:{lote.qtd}")
