import datetime, os
from dotenv import load_dotenv
from sqlalchemy import \
Column, ForeignKey, Integer, String, create_engine, DateTime
from sqlalchemy.orm import declarative_base, relationship

load_dotenv()

url = os.environ['URL_DB']

engine = create_engine(url, echo = True)

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    cpf = Column(String(30), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    count = Column(Integer, nullable=False)
    created_on = Column(DateTime, default=datetime.datetime.now())


Base.metadata.create_all(engine)