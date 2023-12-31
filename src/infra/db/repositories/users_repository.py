from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity

class UsersRepository():
  
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        """Insert data in Users Entity"""
        with DBConnectionHandler() as database:
            try:
                new_registry = UsersEntity(first_name=first_name, last_name=last_name, age=age)
                database.session.add(new_registry)
                database.session.commit() 
              
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    @classmethod
    def select_user(cls, first_name: str) -> any:
        """Select data in Users Entity"""
        with DBConnectionHandler() as database:
            try:
                query = database.session.query(UsersEntity).filter(UsersEntity.first_name == first_name)
                user = query.all()
                database.session.commit()
                return user 
              
            except Exception as exception:
                database.session.rollback()
                raise exception
