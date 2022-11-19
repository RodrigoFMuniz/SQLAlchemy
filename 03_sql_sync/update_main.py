from datetime import datetime
from conf.db_session import create_session
import models.__all_models as md

def atualiza_sabor(id_sabor: int, novo_nome:str)->None:
    with create_session() as session:
        sabor: md.Sabor = session.query(md.Sabor).filter(md.Sabor.id == id_sabor).one_or_none()
        print(sabor)

        if sabor:
            sabor.nome = novo_nome
            sabor.data_criacao = datetime.now()
        
            session.commit()
        else:
            print(f'Sabor não encontrado')

def atualiza_picole(id_picole: int, novo_sabor:str)->None:
    with create_session() as session:
        picole: md.Picole = session.query(md.Picole).filter(md.Picole.id == id_picole).one_or_none()
        print(picole)

        if picole:
            picole.sabor.nome = novo_sabor
            picole.data_criacao = datetime.now()
        
            session.commit()
        else:
            print(f'picole não encontrado')

if __name__ == "__main__":
    # from select_main import select_sabor_filtrado
    # atualiza_sabor(id_sabor=42, novo_nome="Morango")
    # select_sabor_filtrado(id_sabor=42)
    atualiza_picole(id_picole=41, novo_sabor="Maracujá")
    