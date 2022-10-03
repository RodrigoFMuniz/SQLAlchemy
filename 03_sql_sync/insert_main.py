from pydoc import describe
from xml.dom.minidom import Notation
from conf.db_session import create_session

from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.revendedor import Revendedor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole

def insert_aditivo_nutritivo()->AditivoNutritivo:
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

    return an

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

def insert_conservante()->Conservante:
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

    return conservante

def insert_ingrediente()->Ingrediente:
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

    return ingrediente
    
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

def insert_tipo_embalagem()->TipoEmbalagem:
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

    return tipo_embalagem

def insert_tipo_picole()->TipoPicole:
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

    return tipo_picole

def insert_lote()->Lote:
    print("Cadastrando lote")
    id_tipo_picole:int = int(input('Informe o tipo:'))
    qtd:int = int(input('Informe a qtd:'))

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, qtd=qtd)

    with create_session() as session:
        session.add(lote)
        session.commit()
    
    return lote

def insert_nota_fiscal()->NotaFiscal:
    print('Cadastrar uma nota fiscal')
    valor: float = input('Digite o valor da NF: ')
    n_serie: str = input('Digite o número da NF: ')
    descricao: str = input('Descreva os itens: ')
    id_rev: int = input('Código revendedor: ')

    lote_1: Lote = insert_lote()
    lote_2: Lote = insert_lote()

    nf: NotaFiscal = NotaFiscal(valor=valor, numero_serie=n_serie, descricao=descricao, id_revendedor=id_rev)

    nf.lotes.append(lote_1)
    nf.lotes.append(lote_2)

    with create_session() as session:
        session.add(nf)
        session.commit()

        print(f"ID:{nf.id}")
        print(f"Data de criação:{nf.data_criacao}")
        print(f"Valor:{nf.valor}")
        print(f"SN:{nf.numero_serie}")
        print(f"Decrição:{nf.descricao}")
        print(f"Revendedor:{nf.revendedor.razao_social}")
        for ind,l in enumerate(nf.lotes):
            print(f"{ind} -> {l.tipo_picole.nome}")

    return nf


def insert_picoles()->Picole:
    print('Cadastrar um picolé')
    preco: float = input('Digite o preço: ')
    id_sabor: int = input('Sabor: ')
    id_tipo_picole: int = input('Tipo Picole: ')
    id_tipo_embalagem: int = input('Tipo embalagem: ')

    ing:Ingrediente = insert_ingrediente()
    cons: Conservante = insert_conservante()
    an: AditivoNutritivo = insert_aditivo_nutritivo()

    picole: Picole = Picole(preco=preco, id_sabor = id_sabor,id_tipo_picole=id_tipo_picole,id_tipo_embalagem=id_tipo_embalagem)

    picole.ingredientes.append(ing)

    if cons:
        picole.conservantes.append(cons)

    if an:
        picole.aditivo_nutritivo.append(an)
    
    with create_session() as session:
        session.add(picole)

        session.commit()

        print(f"ID:{picole.id}")
        print(f"Data de criação:{picole.data_criacao}")
        print(f"Preço:{picole.preco}")
        print(f"Sabor:{picole.sabor.nome}")
        print(f"Tipo de picolé:{picole.tipos_picole.nome}")
        print(f"Tipo de embalagem:{picole.tipos_embalagem.nome}")
        for i in picole.ingredientes:
            print(f"Ingrediente: {i.id} -> {i.nome}")
        if len(picole.conservantes) > 0:
            for c in picole.conservantes:
                print(f"Conservante: {c.id} -> {c.nome}")
        if len(picole.aditivo_nutritivo) > 0:
            for a in picole.aditivo_nutritivo:
                print(f"Aditivo: {a.id} -> {a.nome}")
        
    return picole



if __name__ == "__main__":
    # insert_aditivo_nutritivo()
    # insert_sabor()
    # insert_conservante()
    # insert_ingrediente()
    # insert_revendedor()
    # insert_tipo_embalagem()
    # insert_tipo_picole()
    # lote = insert_lote()

    # print(f"ID:{lote.id}")
    # print(f"Data de criação:{lote.data_criacao}")
    # print(f"Tipo:{lote.id_tipo_picole}")
    # print(f"Qtd:{lote.qtd}")

    # insert_nota_fiscal()
    insert_picoles()



