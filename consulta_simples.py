import os
import sqlite3

conn = sqlite3.connect("C:/repositorios/banco_de_dados_relacional/meu_banco.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

os.system('cls')
for row in resultados:
    print(row)
conn.close()