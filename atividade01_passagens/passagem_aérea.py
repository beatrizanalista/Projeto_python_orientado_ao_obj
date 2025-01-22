# Atividade 001 - Passagens Aréas
# Curso: Desenvolvimento de sistemas
# Data:29/11
# Autor: Beatriz victoria

# - normalição
# A atividade proposta consiste em desenvolver um sistema de gerenciamento de passagens aéreas utilizando Python e o banco de dados SQLite3,
# aplicando o conceito de CRUD (Create, Read, Update e Delete) para manipulação dos dados. O sistema deve permitir o cadastro de informações essenciais,
# como nome do passageiro, número do voo, destino, data e hora da viagem, preço do bilhete, entre outros detalhes relevantes. Com a estrutura de CRUD,
# os usuários devem poder adicionar novos registros de passagens, visualizar a lista de passagens cadastradas, atualizar informações (por exemplo, ajustar horários ou destinos) e,
# quando necessário, excluir registros de passagens.

import os
import sqlite3
os.system('cls')


def criando_bd():
    conn = sqlite3.connect(
        "..\\banco_de_dados_relacional\\atividade01_passagens\\viajem.db")
    cursor = conn.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS viajante (
        id_viajante INTEGER PRIMARY KEY, 
        nome_viajante TEXT,
        numero_embarque TEXT,
        origem TEXT,
        destino TEXT,
        idade INTEGER
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS companhia_aerea (
        id_companhia INTEGER PRIMARY KEY,
        nome_da_empresa TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classe (
        id_classe INTEGER PRIMARY KEY,
        classe TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS preco (
        id_preco INTEGER PRIMARY KEY,
        preco_da_passagem TEXT,
        tipo TEXT           
        );
    ''')

    cursor.execute('''CREATE TABLE passagem (
        id INTEGER PRIMARY KEY, 
        id_viajante INTEGER,
        id_cadeira INTEGER,
        id_companhia INTEGER,
        id_preco INTEGER,
        id_classe INTEGER, 
        data_ida TEXT,
        data_volta TEXT, 
        assento TEXT,
        portao_embarque TEXT,
        FOREIGN KEY (id_viajante) REFERENCES viajante (id_viajante),
        FOREIGN KEY (id_cadeira) REFERENCES cadeira (id_cadeira),
        FOREIGN KEY (id_companhia) REFERENCES companhia_aerea (id_companhia),
        FOREIGN KEY (id_preco) REFERENCES preco (id_preco),
        FOREIGN KEY (id_classe) REFERENCES classe (id_classe)               
        );
    ''')

    conn.commit()

    conn.close()

    return 'OK!'


# resposta = criando_bd()
# print(resposta)