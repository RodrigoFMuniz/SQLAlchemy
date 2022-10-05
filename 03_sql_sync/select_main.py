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


            


if __name__ == "__main__":
    select_aditivos_nutritivos()
    