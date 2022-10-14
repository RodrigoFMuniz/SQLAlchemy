import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase
import sqlalchemy.orm as orm

from typing import List, Optional

from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole

from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo

#Construção da tabela auxiliar para configuração de relacionamento N:M

ingredientes_picole = sa.Table(
  'ingredientes_picole',
  ModelBase.metadata,
  sa.Column('id_picole',sa.Integer,sa.ForeignKey('picoles.id')),
  sa.Column('id_ingrediente',sa.Integer,sa.ForeignKey('ingredientes.id'))
)

conservantes_picole = sa.Table(
  'conservantes_picole',
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
  id: int = sa.Column(sa.Integer,primary_key=True, autoincrement=True)
  data_criacao: datetime = sa.Column(sa.DateTime,default=datetime.now,index=True)
  preco: float = sa.Column(sa.DECIMAL(6,2), nullable=False)

  #Relacionamento1:1
  id_sabor:int = sa.Column(sa.Integer, sa.ForeignKey('sabores.id'))
  sabor:Sabor = orm.relationship('Sabor',lazy='joined')

  id_tipo_picole: int = sa.Column(sa.String, sa.ForeignKey('tipos_picole.id'))
  tipos_picole:TipoPicole = orm.relationship('TipoPicole', lazy='joined')

  id_tipo_embalagem: int = sa.Column(sa.String, sa.ForeignKey('tipos_embalagens.id'))
  tipos_embalagem: TipoEmbalagem = orm.relationship('TipoEmbalagem', lazy='joined')

  #Relacionamento N:M
  ingredientes: List[Ingrediente] = orm.relationship('Ingrediente', secondary='ingredientes_picole', backref='ingrediente', lazy="joined")

  conservantes: Optional[List[Conservante]] = orm.relationship('Conservante', secondary="conservantes_picole", backref="conservante", lazy="joined")
  
  aditivo_nutritivo: Optional[List[AditivoNutritivo]] = orm.relationship('AditivoNutritivo', secondary="aditivos_nutritivos_picole", backref="aditivo_nutritivo", lazy="joined")

  def __repr__(self)->str:
    return f'<Picolé: {self.tipos_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}'
