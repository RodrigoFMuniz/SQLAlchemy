from typing import Optional
from conf.db_session import create_session

from models.__all_models import Picole, Revendedor

def deletar_picole(id_picole: int)->None:
    with create_session() as session:
        picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            session.delete(picole)
            session.commit()

        else:
            print(f"Não encontrei id {id_picole}")

def deletar_revendedor(id_revendedor:int)->None:
    with create_session() as session:
        revendedor: Revendedor = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            session.delete(revendedor)
            session.commit()
        else:
            print(f"Revendedor id {id_revendedor} não existe no banco de dados")


if __name__ == "__main__":

    from select_main import select_complexo_picole_by_id
    from select_main import select_revendedor_by_id
    from select_main import select_nota_fiscal

    # id_picole_filtrado = select_complexo_picole_by_id(id_picole=40)
    # print(id_picole_filtrado)

    # deletar_picole(id_picole=0)

    # id_picole_after= select_complexo_picole_by_id(id_picole=40)
    # print(id_picole_after)

    # id_rev = select_revendedor_by_id(id_revendedor=2)

    # deletar_revendedor(id_revendedor=id_rev.id)

    # id_rev = select_revendedor_by_id(id_revendedor=2)

    id_rev = select_revendedor_by_id(id_revendedor=4)
    print(id_rev)

    deletar_revendedor(id_revendedor=id_rev.id)

    id_rev = select_revendedor_by_id(id_revendedor=4)
    print(id_rev)




