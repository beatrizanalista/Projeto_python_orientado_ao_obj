import os 
import sqlite3


conn = sqlite3.connect(""C:/repositorio_beatriz/banco_de_dados_relacional/atividade01_passagens/viajem.db"")
cursor = conn.cursor()

os.system('cls')


pergunta = input("qual tabela você deseja consultar? ")

if pergunta == "viajante":
    nome_viajante = input("Digite o nome do viajante para se apagar: ")

    cursor.execute("DELETE FROM  viajante WHERE nome = ?", (nome_viajante,))
    conn.commit()

    print("o viajante foi apagado com sucesso!")

    conn.close()
    
    
elif pergunta == "site":
    nome_cupom = input("Digite a promoção do cupom que não será usado: ")

    cursor.execute("DELETE FROM site WHERE cupons = ?", (nome_cupom,))
    conn.commit()

    print("o cupom foi apagado!")

    conn.close()
    
    
elif pergunta == "destino":
    destino = input("Digite o destino que você deseja remover: ")

    cursor.execute("DELETE FROM destino WHERE destino = ?", (destino,))
    conn.commit()

    print("o destino foi removido!")

    conn.close()
    
    
elif pergunta == "passagem":
    assento = input("Digite o assento que deseja remover: ")

    cursor.execute("DELETE FROM passagem WHERE assento = ?", (assento,))
    conn.commit()

    print("A passagem foi cancelada com sucesso!")

    conn.close()
