import os
import sqlite3 
from prettytable import PrettyTable # no terminal: pip install prettytable

conn = sqlite3.connect("C:/repositorios/banco_de_dados_relacional/meu_banco.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

os.system('cls')

# cria a tabela prettyTable e define os nomes das colunas
tabela = PrettyTable()

colunas = [descricao[0] for descricao in cursor.description]

tabela.field_names = colunas

for row in resultados:
    tabela.add_row(row)
    
    
print(tabela)
conn.close()

