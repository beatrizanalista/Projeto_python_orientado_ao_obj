import os
import sqlite3


os.system('cls')


def atualizar(Atualizar):
    conn = sqlite3.connect(
        "..\\banco_de_dados_relacional\\atividade01_passagens\\viajem.db")
    cursor = conn.cursor()
    if Atualizar == "viajante":

        nome_viajante = input("digite o nome do viajante: ")
        novo_numero = int(input("digite a novo numero: "))

        cursor.execute("UPDATE viajante SET nome = ? WHERE nome = ?",
                       (novo_numero, nome_viajante))

    elif Atualizar == "companhia_aerea":
        nome_companhia = input("digite o nome da companhia aerea: ")
        novo_cupom = input("digite a novo cupom para o desconto: ")

        cursor.execute("UPDATE site SET cupons = ? WHERE companhias = ?",
                       (novo_cupom, nome_companhia))

    elif Atualizar == "classe":
        assento_atual = input("digite o assento atual: ")
        novo_assento = input("digite o novo assento que será usado: ")

        cursor.execute("UPDATE classe SET assento_atual = ? WHERE assento = ?",
                       (novo_assento, assento_atual))

    elif Atualizar == "passagem":
        nome_viajante = input("digite o nome do viajante: ")
        nova_data = input("digite a nova data: ")

        cursor.execute("UPDATE passagem SET data = ? WHERE nome_do_viajante = ?",
                       (nova_data, nome_viajante))

    elif Atualizar == "preco":
        preco_atual = input("digite o preco atual para modificar: ")
        novo_preco = input("digite o novo preco: ")

        cursor.execute("UPDATE passagem SET data = ? WHERE nome_do_viajante = ?",
                       (novo_preco, preco_atual))

        conn.commit()
        conn.close()
        print("Atualização Feita!")
