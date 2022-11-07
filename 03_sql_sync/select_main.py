from ssl import SSLSession
from typing import List
from sqlalchemy import func
import sqlalchemy as sa
from conf.helpers import formata_data
from conf.db_session import create_session

# select simples

import models.__all_models as md

def select_aditivos_nutritivos()->None:
    with create_session() as session:
        aditivos_nutritivos:List[md.AditivoNutritivo] = session.query(md.AditivoNutritivo).limit(5)
        
        for an in aditivos_nutritivos:
            print(f"ID: {an.id}")
            print(f"Data: {formata_data(an.data_criacao)}")
            print(f"Nome: {an.nome}")
            print(f"Fórmula química: {an.formula_quimica}")

def select_sabor()->None:
    with create_session() as session:
        sabor:List[md.Sabor] = session.query(md.Sabor)

        for sa in sabor:
            print(f"ID: {sa.id}")
            print(f"Data: {formata_data(sa.data_criacao)}")
            print(f"Nome: {sa.nome}")
            
def select_revendedor()->None:
    with create_session() as session:
        revendedor: List[md.Revendedor] = session.query(md.Revendedor)

        for rev in revendedor:
            print(f"ID: {rev.id}")
            print(f"Data: {formata_data(rev.data_criacao)}")
            print(f"CNPJ: {rev.cnpj}")
            print(f"Razão social: {rev.razao_social}")
            print(f"Contato: {rev.contato}")

def select_revendedor_by_id(id_revendedor:int)->md.Revendedor:
    with create_session() as session:
        revendedor: md.Revendedor = session.query(md.Revendedor).filter(md.Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            return revendedor
        else:
            print(f"ID {id_revendedor} não encontrado")

def select_ingrediente()->None:
    with create_session() as session:
        ingrediente: List[md.Ingrediente] = session.query(md.Ingrediente).limit(10)
    
        for ing in ingrediente:
            print(f"ID: {ing.id}")
            print(f"Data: {formata_data(ing.data_criacao)}")
            print(f"Nome: {ing.nome}")

def select_conservante()->None:
    with create_session() as session:
        conservante: List[md.Conservante] = session.query(md.Conservante)

        for c in conservante:
            print(f"ID: {c.id}")
            print(f"Data: {formata_data(c.data_criacao)}")
            print(f"Nome: {c.nome}")
            print(f"Descrição: {c.descricao}")

def select_tipo_embalagem()->None:
    with create_session() as session:
        tipo_embalagem: List[md.TipoEmbalagem] = session.query(md.TipoEmbalagem)

        for tp in tipo_embalagem:
            print(f"ID: {tp.id}")
            print(f"Data: {formata_data(tp.data_criacao)}")
            print(f"Nome: {tp.nome}")

def select_tipo_picole()->None:
    with create_session() as session:

        tipo_picole: List[md.TipoPicole] = session.query(md.TipoPicole)

        for tp in tipo_picole:
            print(f"ID: {tp.id}")
            print(f"Data: {formata_data(tp.data_criacao)}")
            print(f"Nome: {tp.nome}")

# Queries com filtro

def select_sabor_filtrado(id_sabor: int) ->None:
    with create_session() as session:
        #forma 1
        # sabor_first: md.Sabor = session.query(md.Sabor).filter(md.Sabor.id == id_sabor).first()
        #forma 2
        # sabor_first: md.Sabor = session.query(md.Sabor).filter(md.Sabor.id == id_sabor).one_or_none()
        # Forma 3
        # sabor_first: md.Sabor = session.query(md.Sabor).filter(md.Sabor.id == id_sabor).one()
        # Forma 4: Usando whery ao invés de filter, com os métodos auxiliares first(), one_or_none) e one().
        sabor_first: md.Sabor = session.query(md.Sabor).where(md.Sabor.id == id_sabor).first()


        if sabor_first:
            print(f"Sabor filtrado ID: {sabor_first.id}")
            print(f"Sabor filtrado Nome: {sabor_first.nome}")
            print(f"Sabor filtrado Data: {formata_data(sabor_first.data_criacao)}")
        
        else:
            raise Exception('Error de tipo')
            # print('Error de tipo')


# Tipos complexos

def select_complexo_picole()->None:
    with create_session() as session:
        picoles:List[md.Picole] = session.query(md.Picole).all()
        
        for picole in picoles:
            print(f"ID: {picole.id}")
            print(f"Data: {formata_data(picole.data_criacao)}")
            print(f"Preço: {picole.preco}")
            print(f"Sabor: {picole.sabor.nome}")
            print(f"Tipo de embalagem: {picole.tipos_embalagem.nome}")
            print(f"Tipo de picole: {picole.tipos_picole.nome}")
            print("Ingredientes")
            for ingrediente in picole.ingredientes:
                print(f"\tIngrediente: {ingrediente.nome}")
            print("Conservantes")
            for conservante in picole.conservantes:
                print(f"\tConservante: {conservante.nome}")
            print("Aditivos Nutritivos")
            for ad in picole.aditivo_nutritivo:
                print(f"\tAditivo: {ad.formula_quimica}")

def select_complexo_picole_by_id(id_picole:int)->None:
    with create_session() as session:
        picole:md.Picole | None= session.query(md.Picole).filter(md.Picole.id == id_picole).one_or_none()
        
        return picole
         
                
def select_complexo_sabor()->None:
    with create_session() as session:
        sabores: List[md.Sabor] = session.query(md.Sabor).order_by(md.Sabor.data_criacao.desc(), md.Sabor.nome).all()

        for sabor in sabores:
            print(f"ID: {sabor.id}")
            print(f"Data: {formata_data(sabor.data_criacao)}")
            print(f"Sabor: {sabor.nome}")
        
def select_complexo_sabor_limit()->None:
    with create_session() as session:
        sabores: List[md.Sabor] = session.query(md.Sabor).order_by(md.Sabor.data_criacao.desc()).limit(25)

        for sabor in sabores:
            print(f"ID: {sabor.id}")
            print(f"Data: {formata_data(sabor.data_criacao)}")
            print(f"Sabor: {sabor.nome}")

def select_complexo_sabor_qtd()->None:
    with create_session() as session:
        qtd_sabor: int = session.query(md.Sabor).count()

        print(f"Qtd: {qtd_sabor}")

def select_agregation()->None:
    with create_session() as session:
        resultado: List = session.query(
            func.sum(md.Picole.preco).label('soma'),
            func.avg(md.Picole.preco).label('media'),
            func.min(md.Picole.preco).label('mais_barato'),
            func.max(md.Picole.preco).label('mais_caro')
        ).all()

        print(f"Resultado: {resultado}")

        print(
            f"Resultado da soma: {resultado[0][0]}\n"
            f"Resultado da media: {resultado[0][1]}\n"
            f"Resultado da min: {resultado[0][2]}\n"
            f"Resultado da max: {resultado[0][3]}\n"
        )


def select_nota_fiscal(id_nf: int)-> md.NotaFiscal:
    with create_session() as session:
        nf: md.NotaFiscal = session.query(md.NotaFiscal).filter(md.NotaFiscal.id == id_nf).one_or_none()

        print(f"ID: {nf.id}")
        print(f"Data: {formata_data(nf.data_criacao)}")
        print(f"NS: {nf.numero_serie}")
        print(f"Valor: {nf.valor}")
        print(f"Descrição: {nf.descricao}")
        print(f"Revendedor: {nf.revendedor.razao_social}")
        for l in nf.lotes:
            print(f"Tipo Picolé{l.tipo_picole}")
            print(f"Quantidade{l.qtd}")
        
        return nf


if __name__ == "__main__":
    # select_aditivos_nutritivos()
    # select_sabor()
    # select_revendedor()
    select_ingrediente()
    # select_conservante()
    # select_tipo_embalagem()
    # select_tipo_picole()
    # select_sabor_filtrado(id_sabor=23)
    # select_complexo_picole()
    # select_complexo_sabor_qtd()
    # select_agregation()
    # select_nota_fiscal(id_nf=3)
    