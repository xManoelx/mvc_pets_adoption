"""Funcoes de conexao com o banco de dados"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    """Classe para gerenciar conexão com o banco de dados"""

    # Método construtor
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None

    # Funcao para conectar ao banco de dados
    def connect_to_db(self):
        """Conecta ao banco de dados"""
        self.__engine = create_engine(self.__connection_string)

    # Funcao para obter o engine de conexao
    def get_engine(self):
        """Retorna o engine de conexão"""
        return self.__engine

    # Funcao para criar uma secao com o banco de dados
    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self
    
    # Funcao para fechar a secao com o banco de dados
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

db_connection_handler = DBConnectionHandler()
