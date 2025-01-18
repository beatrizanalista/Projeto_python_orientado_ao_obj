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
        data_ida = input("Insira a data da ida:")
        data_volta = input("Insira a data da volta:")
        assento = input("Informe o assento:")
        portao_embarque = input("Qual será o portão de embarque:")
        classe = input("Qual foi a classe escolhida:")
        cursor.execute(
            'INSERT INTO passagem (id_viajante,id_cadeira,id_companhia,id_preco, data_ida,data_volta, assento,portao_embarque, classe ) values  (?,?,?,?,?,?,?,?,?)', (id_viajante, id_cadeira, id_companhia, id_preco, data_volta, data_ida, assento, portao_embarque, classe,))

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
        id_classe = input("Insira o id da classe aerea: ")
        classe = input("Insira a classe do assento: ")
        cursor.execute(
            ' INSERT INTO classe (id_classe, classe) values(?,?)', (id_classe, classe,))

        conn.commit()
        conn.close()

    if adicionar == "preco":
        preco_da_passagem = input("O preço da passagem é: ")
        tipo = input("Tipo da classe escolhida: ")
        cursor.execute(
            ' INSERT INTO preco (id,preco_da_passagem,tipo) values (?,?)', preco_da_passagem, tipo,)

        conn.commit()
        conn.close()

# adicionar_passagem()


print("Adicionado com sucesso!")
