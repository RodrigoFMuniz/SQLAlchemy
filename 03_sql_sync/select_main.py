from typing import List
from sqlalchemy import func
from conf.helpers import formata_data
from conf.db_session import create_session

# select simples

import models.__all_models as md

def select_aditivos_nutritivos()->None:
    with create_session() as session:
        aditivos_nutritivos:List[md.AditivoNutritivo] = session.query(md.AditivoNutritivo)

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

def select_ingrediente()->None:
    with create_session() as session:
        ingrediente: List[md.Ingrediente] = session.query(md.Ingrediente)

        for ing in ingrediente:
            print(f"ID: {ing.id}")
            print(f"Data: {formata_data(ing.data_criacao)}")
            print(f"Nome: {ing.nome}")
        

if __name__ == "__main__":
    # select_aditivos_nutritivos()
    # select_sabor()
    # select_revendedor()
    select_ingrediente()
    