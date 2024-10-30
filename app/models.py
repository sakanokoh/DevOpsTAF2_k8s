from sqlalchemy import Column, Integer, String
from .database import Base

# Définir un modèle pour la table "Student"
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
