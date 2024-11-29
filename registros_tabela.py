import sqlite3 

# Conexão com o banco de dados
conn = sqlite3.connect("C:/repositorios/banco_de_dados_relacional/meu_banco.db")

cursor = conn.cursor()

dados_varios_clientes = [
    ("Maria Souza", 25),
    ("Carlos Pereira", 35),
    ("Pedro José", 28),
    ("Ana Costa", 28),
    ("Luis Gomes", 30),
    ("Fernada Lima", 22),
    ("Roberto Silva", 40),
    ("Juliana Almeida", 33),
    ("Lucas Martins", 27),
    ("Sofia Ferreira", 31)
]

cursor.executemany(
    "INSERT INTO clientes (nome, idade) VALUES (?, ?)", dados_varios_clientes)
conn.commit()

conn.close()