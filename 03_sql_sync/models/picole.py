import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase
import sqlalchemy.orm as orm
from typing import List

from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante

#Construção da tabela auxiliar para configuração de relacionamento N:M

ingredientes_picole = sa.Table(
  'ingredientes_picole',
  ModelBase.metadata,
  sa.Column('id_picole',sa.Integer,sa.ForeignKey('picoles.id')),
  sa.Column('id_ingrediente',sa.Integer,sa.ForeignKey('ingredientes.id'))
)

conservantes_picoles = sa.Table(
  'conservantes_picoles',
  ModelBase.metadata,
  sa.Column('id_picole',sa.Integer,sa.ForeignKey('picoles.id')),
  sa.Column('id_conservante',sa.Integer,sa.ForeignKey('conservantes.id'))
)

aditivos_nutritivos_picole = sa.Table(
  'aditivos_nutritivos_picole',
  ModelBase.metadata,
  sa.Column('id_picole',sa.Integer,sa.ForeignKey('picoles.id')),
  sa.Column('id_aditivo_nutritivo',sa.Integer,sa.ForeignKey('aditivos_nutritivos.id'))
)

class Picole(ModelBase):
  __tablename__:str = 'picoles'
  id: int = sa.Column(sa.BigInteger,primary_key=True, autoincrement=True)
  data_criacao: datetime = sa.Column(sa.DateTime,default=datetime.now,index=True)
  preco: float = sa.Column(sa.DECIMAL(6,2), nullable=False)

  #Relacionamento1:1
  id_sabor:int = sa.Column(sa.Integer, sa.ForeignKey('sabores.id'))
  sabor:Sabor = orm.relationship('Sabor',lazy='joined')

  id_tipo_picole: int = sa.Column(sa.String, sa.ForeignKey('tipos_picole.id'))
  tipos_picole:TipoPicole = orm.relationship('TipoPicole', lazy='joined')

  id_tipo_embalagem: int = sa.Column(sa.String, sa.ForeignKey('tipos_embalagem.id'))
  tipos_embalagem: TipoEmbalagem = orm.relationship('TipoEmbalagem', lazy='joined')

  #Relacionamento N:M

  ingredientes:List[Ingrediente] = orm.relationship('Ingrediente', secondary=ingredientes_picole, backref='ingrediente', lazy='joined')

  conservantes:List[Conservante] = orm.relationship('Conservante')

  def __repr__(self)->str:
    return f'<Picolé: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.nome}'
