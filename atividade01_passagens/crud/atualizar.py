import os 
import sqlite3


conn = sqlite3.connect("C:/repositorio_beatriz/banco_de_dados_relacional/atividade01_passagens/viajem.db")
cursor = conn.cursor()

os.system('cls')

Atualizar = ("qual tabela você deseja Atualizar? ")

if Atualizar  == "cliente":

    nome_viajante = input("digite o nome do viajante: ")
    novo_numero = int(input("digite a novo numero: "))

    cursor.execute("UPDATE viajante SET telefone = ? WHERE nome = ?",
                    (novo_numero, nome_viajante))

elif Atualizar  == "site":
    nome_companhia = input("digite o nome da companhia aerea: ")
    novo_cupom = input("digite a novo cupom para o desconto: ")

    cursor.execute("UPDATE site SET cupons = ? WHERE companhias = ?",
                    (novo_cupom, nome_companhia))
    
elif Atualizar  == "destino":
    atual_destino = input("digite o atual destino: ")
    novo_destino = input("digite o novo destino para onde deseja ir: ")

    cursor.execute("UPDATE destino SET novo_destino = ? WHERE locais = ?",
                    (novo_destino, nome_destino))

elif Atualizar  == "passagem":
    nome_viajante = input("digite o nome do viajante: ")
    nova_data = input("digite a nova data: ")

    cursor.execute("UPDATE passagem SET data = ? WHERE nome_do_viajante = ?",
                    (nova_data, nome_viajante))


conn.commit()
conn.close()
print("Atualização Feita!")