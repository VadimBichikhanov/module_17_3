from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
import sys
import os

# Добавляем путь к директории проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.db import Base, engine

class Task(Base):
    __tablename__ = "task"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    status = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship("User", back_populates="tasks")

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Пример использования
print(CreateTable(Task.__table__).compile(engine))