from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

# Classe que representa a tabela 'pets' no banco de dados SQLite
class PetsTable(Base):
    __tablename__ = 'pets'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    type = Column(String(100), nullable=False)

    # Representação em string do objeto PetsTable
    def __repr__(self):
        return f'Pets [name={self.name}, type={self.type}]'
