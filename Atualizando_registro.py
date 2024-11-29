import os
import sqlite3

conn = sqlite3.connect("c:/repositorios/banco_de_dados_relacional/meu_banco.db")

cursor = conn.cursor()

os.system('cls')
nome_cliente = input("Digite o nome do cliente: ")
nova_idade = int(input("Digite a nova idade: "))

cursor.execute("UPDATE clientes SET idade = ? WHERE nome = ?",
               (nova_idade, nome_cliente))

conn.commit()
print("Dados atualizados com sucesso!")
conn.close()