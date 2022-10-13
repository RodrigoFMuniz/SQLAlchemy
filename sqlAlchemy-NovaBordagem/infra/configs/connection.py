from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configs.base import BASE

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = f'sqlite:///db/cinema.sqlite'
        self.__engine = self.__create_database_engine()
        self.session = None
    
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string, echo=True, connect_args={"check_same_thread":False})
        return engine

    def get_engine(self):
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
