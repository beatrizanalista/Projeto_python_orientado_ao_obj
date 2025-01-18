import os
import sqlite3


os.system('cls')


def apagar(pergunta):
    conn = sqlite3.connect(
        "..\\banco_de_dados_relacional\\atividade01_passagens\\viajem.db")
    cursor = conn.cursor()
    if pergunta == "viajante":
        nome_viajante = input("Digite o nome do viajante para se apagar: ")
        numero_embarque = input("Digite qual o numero do embarque para apagar: ")
        idade_viajante = input("Digite a idade para se apagar: ")
        cursor.execute("DELETE FROM  viajante WHERE nome = ?",
                       (nome_viajante, numero_embarque, idade_viajante))
        conn.commit()

        print("O viajante foi apagado com sucesso!")

        conn.close()

    elif pergunta == "classe":
        nome_cupom = input("Digite a promoção do cupom que não será usado: ")

        cursor.execute(
            "DELETE FROM site WHERE cupons = ?", (nome_cupom,))
        conn.commit()

        print("O cupom foi apagado!")

        conn.close()

    elif pergunta == "companhia_aerea":
        destino = input("Digite o destino que você deseja remover: ")

        cursor.execute(
            "DELETE FROM destino WHERE destino = ?", (destino,))
        conn.commit()

        print("O destino foi removido!")

        conn.close()

    elif pergunta == "passagem":
        assento = input("Digite o assento que deseja remover: ")
        data_ida = input("Digite data da ida para apagar: ")
        data_volta = input("Digite a data volta para apagar: ")
        cursor.execute("DELETE FROM passagem WHERE assento = ?", (assento, data_ida, data_volta))
        conn.commit()

        print("Foi cancelado com sucesso!")

    elif pergunta == "preço":
        preco = input("Digite o preço que você deseja apagar: ")

        cursor.execute(
            "DELETE FROM preco WHERE preco_da_passagem = ?", (preco,))
        conn.commit()

        print("O preço da passagem foi removido!")

        conn.close()
