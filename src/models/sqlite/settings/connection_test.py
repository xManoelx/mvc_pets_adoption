"""Testes para conexão com o banco de dados"""

import pytest
from sqlalchemy.engine import Engine
from .connection import db_connection_handler


# Teste para a funcao de conexao ao banco de dados
@pytest.mark.skip(
    reason="Interação com o banco de dados real, "
    "ignorando durante os testes automatizados."
)
def test_connect_to_db():
    """Testa a conexão com o banco de dados"""
    assert db_connection_handler.get_engine() is None

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
