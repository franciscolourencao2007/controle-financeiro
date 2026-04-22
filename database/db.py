import sqlite3

# Nome do banco de dados
DB_NAME = "finance.db"

def conectar():
    """Cria e retorna uma conexão com o banco de dados."""
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    """Cria a tabela de transações caso ela não exista."""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            tipo TEXT NOT NULL,
            data TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def listar_transacoes():
    """Retorna todas as transações cadastradas no banco de dados."""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, descricao, valor, tipo, data
        FROM transacoes
        ORDER BY id DESC
    """)

    transacoes = cursor.fetchall()
    conn.close()
    return transacoes
def excluir_transacao(transacao_id):
    """Exclui uma transação do banco de dados pelo ID."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transacoes WHERE id = ?", (transacao_id,))
    conn.commit()
    conn.close()