from configs.connection import DBConnectionHandler
from entities.usuarios import User

class UserRepository:
    def select_all_users(self) -> None:
        with DBConnectionHandler() as db:
            data = db.session.query(User).all()
            for d in data:
                print(d.name)
                print(d.surname)
                print(d.cpf)
    
    def insert_user(self,user: User)-> None:
        with DBConnectionHandler() as db:
            if len(user.name)>50:
                data = ValueError("Error: Número máximo extrapolado")
                print(data)
            else:
                db.session.add(user)
                db.session.commit()