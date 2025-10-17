
from sqlalchemy import Column, String
from datetime import datetime


from sqlalchemy.orm import as_declarative
from sqlalchemy import Column, Integer, DateTime, func




@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True)


class User(Base):
    __tablename__ = 'user'
    
    created_at = Column(DateTime, index=True, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), server_onupdate=func.now(), onupdate=datetime.now)
    
    username = Column(String(128), index=True, nullable=False)
    first_name= Column(String(64))
    lastname=Column(String(64))
    age = Column(Integer, nullable=False)



