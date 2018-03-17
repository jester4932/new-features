from sqlalchemy import create_engine, Column, Integer, VARCHAR, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///newfeatures.db',  echo=True)
Base = declarative_base()


class Features(Base):
    __tablename__= 'features'

    id = Column(Integer, Sequence('user_id_seq'),  primary_key=True)
    title = Column(VARCHAR(25))
    description = Column(VARCHAR(100))
    client = Column(VARCHAR(50))
    priority = Column(Integer)
    targetdate = Column(VARCHAR(10))
    productarea = Column(VARCHAR(20))

    def __repr__(self):
        return "{%s:{ title : '%s', description : '%s', client : '%s', priority : '%s', targetdate : '%s', productarea : '%s'}" % (
            self.id, self.title, self.description, self.client, self.priority, self.targetdate, self.productarea)

def db_connection():
    try:
        x = sessionmaker(bind=engine)
        session = x()
        return session
    except Exception as exc:
        print exc


Features.__table__
Base.metadata.create_all(engine)
