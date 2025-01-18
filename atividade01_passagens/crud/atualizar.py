import os
import sqlite3


os.system('cls')


def atualizar(Atualizar):
    conn = sqlite3.connect(
        "..\\banco_de_dados_relacional\\atividade01_passagens\\viajem.db")
    cursor = conn.cursor()
    if Atualizar == "viajante":

        nome_viajante = input("Digite o nome do viajante: ")
        novo_numero = int(input("Digite a novo numero para o embarque: "))
        nova_origem = input("Digite a nova origem da viajem: ")
        novo_destino = input("Digite o novo destino escolhido: ")
        nova_idade = input("insira a idade correta: ")
        cursor.execute("UPDATE viajante SET nome_viajante = ? WHERE nome_viajante = ?",
                       (novo_numero, nome_viajante,nova_origem, novo_destino, nova_idade))

    elif Atualizar == "companhia aerea":
        nome_companhia = input("Digite o novo nome da companhia aerea: ")
        id_companhia = int(input("Digite o ID da companhia: "))

        cursor.execute("UPDATE companhia_aerea SET nome_da_empresa = ? WHERE id_companhia = ?", (nome_companhia, id_companhia))


    elif Atualizar == "classe":
        assento_atual = input("digite o assento atual: ")
        novo_assento = input("digite o novo assento que será usado: ")

        cursor.execute("UPDATE classe SET assento_atual = ? WHERE assento = ?",
                       (novo_assento, assento_atual))

    elif Atualizar == "passagem":
        nome_viajante = input("Digite o nome do viajante: ")
        nova_data = input("Digite a nova data para a viajem: ")
        nova_data_volta = input("Digite a nova data da volta: ")
        nova_data_ida = input("Digite a nova data da ida: ")
        nova_classe = input("Digite a nova classe a ser escolhida: ")
        novo_assento = input("Digite o novo assento: ")
        cursor.execute("UPDATE passagem SET data = ? WHERE nome_do_viajante = ?",
                       (nova_data, nome_viajante, nova_data, nova_data_volta, nova_data_ida, nova_classe))

    elif Atualizar == "preco":
        preco_atual = input("Digite o preco atual da passagem para atualizar: ")
        novo_preco = input("Digite o novo preco desejado: ")

        cursor.execute("UPDATE passagem SET data = ? WHERE nome_viajante = ?",
                       (novo_preco, preco_atual))

    conn.commit()
    conn.close()
    print("Atualização Feita!")
