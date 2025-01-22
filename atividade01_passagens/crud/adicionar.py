import os
import sqlite3
os.system('cls')


def adicionar(adicionar):
    conn = sqlite3.connect(
        "..\\banco_de_dados_relacional\\atividade01_passagens\\viajem.db")

    cursor = conn.cursor()
    if adicionar == "passagem":
        
        id_viajante = input("Insira o id do viajante:")
        id_cadeira = input("Insira o id da cadeira:")
        id_companhia = input("Insirao id da companhia:")
        id_preco = input("Insira o id do preço:")
        id_classe = input("Qual foi a classe escolhida:")
        data_ida = input("Insira a data da ida:")
        data_volta = input("Insira a data da volta:")
        assento = input("Informe o assento:")
        portao_embarque = input("Qual será o portão de embarque:")
        cursor.execute(
            'INSERT INTO passagem (id_viajante, id_cadeira, id_companhia, id_preco, id_classe, data_ida, data_volta, assento, portao_embarque) values  (?,?,?,?,?,?,?,?,?)', (id_viajante, id_cadeira, id_companhia, id_preco, id_classe, data_ida, data_volta, assento, portao_embarque,))

        conn.commit()
        conn.close()    
        
    if adicionar == "viajante":
        nome_viajante = input("Insira o nome do viajante: ")
        numero_embarque = input("Insira o numero do embarque para o voo: ")
        origem = input("Insira a origem do voo: ")
        destino = input("Insira o destino para a viajem: ")
        idade = input("Qual a idade da pessoa que irá viajar: ")
        cursor.execute(
            ' INSERT INTO viajante (nome_viajante ,numero_embarque,origem ,destino,idade) values (?,?,?,?,?)', (nome_viajante, numero_embarque, origem, destino, idade,))

        conn.commit()
        conn.close()

    if adicionar == "companhia aerea":
        nome_da_empresa = input("Insira o nome da empresa do voo: ")
        cursor.execute(
            ' INSERT INTO companhia_aerea (nome_da_empresa) values (?) ', (nome_da_empresa,))

        conn.commit()
        conn.close()

    if adicionar == "classe":
        classe = input("Insira o tipo de serviço: ")
        cursor.execute(
            ' INSERT INTO classe (classe) values(?)', (classe,))

        conn.commit()
        conn.close()

    if adicionar == "preco":
        preco_da_passagem = input("O preço da passagem é: ")
        tipo = input("Tipo da classe escolhida: ")
        cursor.execute(
            ' INSERT INTO preco (preco_da_passagem, tipo) values (?,?)', (preco_da_passagem, tipo,))

        conn.commit()
        conn.close()

# adicionar_passagem()


print("Adicionado com sucesso!")
