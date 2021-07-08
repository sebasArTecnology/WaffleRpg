from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    account_id = Column(String)
    created = Column(DateTime)
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}({self.account_id}, {self.created})>"


class DataBase:
    def __init__(self, name="db"):
        self.engine = create_engine(f"sqlite:///{name}.sqlite3")
        self.session_maker = sessionmaker(bind = self.engine)
        self.session = self.session_maker()

        self.isNew = not self.engine.dialect.has_table(
            self.engine.connect(), "statement"
        )
        
        if self.isNew:
            Base.metadata.create_all(self.engine)

    def insert(self, model: object):
        self.session.add(model)

    def query(self, model: object, filter_by: object):
        return self.session.query(model).filter(filter_by)
        
    def commit(self):
        self.session.commit()
