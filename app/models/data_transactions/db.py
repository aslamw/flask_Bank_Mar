import datetime, os
from dotenv import load_dotenv
from sqlalchemy import \
Column, Integer, String, create_engine, \
DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from ..data_users.db import Users

load_dotenv()

url = os.environ['T_URL_DB']
engine = create_engine(url, echo = True)
Base = declarative_base()

class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey(Users.id))
    id_user_T = Column(Integer, ForeignKey(Users.id))
    type_transaction = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    created_on = Column(DateTime, default=datetime.datetime.now())
    
    
Base.metadata.create_all(engine)