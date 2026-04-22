from database.db import conectar

class Transacao:
    def __init__(self, descricao, valor, tipo, data, id=None):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo
        self.data = data

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO transacoes (descricao, valor, tipo, data) VALUES (?, ?, ?, ?)",
            (self.descricao, self.valor, self.tipo, self.data)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def atualizar(id, descricao, valor, tipo):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE transacoes SET descricao = ?, valor = ?, tipo = ? WHERE id = ?",
            (descricao, valor, tipo, id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def excluir(id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transacoes WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, descricao, valor, tipo, data FROM transacoes ORDER BY id DESC"
        )
        registros = cursor.fetchall()
        conn.close()
        return registros

    @staticmethod
    def calcular_saldo():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT SUM(
                CASE
                    WHEN tipo = 'Entrada' THEN valor
                    ELSE -valor
                END
            ) FROM transacoes
        """)
        resultado = cursor.fetchone()[0]
        conn.close()
        return resultado if resultado else 0.0