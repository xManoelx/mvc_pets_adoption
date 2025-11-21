from sqlalchemy import Column, String, BIGINT, ForeignKey
from src.models.sqlite.settings.base import Base

# Classe que representa a tabela 'people' no banco de dados SQLite
class PeopleTable(Base):
    __tablename__ = 'people'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    age = Column(BIGINT, nullable=False)
    pet_id = Column(BIGINT, ForeignKey('pets.id'), nullable=True)

    # Representação em string do objeto PeopleTable
    def __repr__(self):
        return (
            f'People [first_name={self.first_name}, '
            f'last_name={self.last_name}, age={self.age}]'
        )
