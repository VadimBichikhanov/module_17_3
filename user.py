from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.schema import CreateTable
import sys
import os

# Добавляем путь к директории проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.db import Base, engine


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")
    
print(CreateTable(User.__table__).compile(engine))