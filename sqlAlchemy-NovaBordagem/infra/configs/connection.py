from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from configs.base import BASE

class DBConnectionHandler:

    def __init__(self) -> None:
        # self.__connection_string: str = f'sqlite:///db/cinema.sqlite'
        self.__connection_string: str = f'mysql+pymysql://dev:dev@localhost:3306/cinema'
        self.__engine: Engine = self.__create_database_engine()
        self.session = None
    
    def __create_database_engine(self) -> Engine:
        # engine = create_engine(self.__connection_string, echo=True, connect_args={"check_same_thread":False})
        engine = create_engine(self.__connection_string, echo=True)
        return engine

    def get_engine(self) -> Engine:
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
    
    def create_table(self):
        engine = self.get_engine()
        BASE.metadata.create_all(engine)
    
    def reset_tables(self):
        engine = self.get_engine()
        BASE.metadata.drop_all(engine)
        BASE.metadata.create_all(engine)

    def delete_tables(self)->None:
        engine = self.get_engine()
        BASE.metadata.drop_all(engine)
