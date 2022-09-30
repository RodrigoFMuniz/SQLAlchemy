import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase
import sqlalchemy.orm as orm
from models.tipo_picole import TipoPicole

class Lote(ModelBase):
  __tablename__:str = 'lotes'

  id:int = sa.Column(sa.BigInteger,primary_key=True, autoincrement=True)
  data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

  id_tipo_picole: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_picole.id'))# table.campo
  tipo_picole: TipoPicole = orm.relationship('TipoPicole',lazy='joined') # Conf interna do sqlalchemy    
  qtd: int = sa.Column(sa.Integer, nullable=False)

  def __repr__(self)->str:
    return f"<Lote: {self.id}>"