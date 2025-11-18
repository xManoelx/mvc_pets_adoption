"""Funcoes de conexao com o banco de dados"""

from sqlalchemy import create_engine

class DBConnectionHandler:
    """Classe para gerenciar conexão com o banco de dados"""

    # Método construtor
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None

    # Funcao para conectar ao banco de dados
    def connect_to_db(self):
        """Conecta ao banco de dados"""
        self.__engine = create_engine(self.__connection_string)

    # Funcao para obter o engine de conexao
    def get_engine(self):
        """Retorna o engine de conexão"""
        return self.__engine


db_connection_handler = DBConnectionHandler()
