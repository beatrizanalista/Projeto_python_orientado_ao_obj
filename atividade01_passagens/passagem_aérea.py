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
        "C:/repositorio_beatriz/banco_de_dados_relacional/atividade01_passagens/viajem.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE passagem (
    id integer PRIMARY KEY, 
    id_viajante integer,
    id_cadeira integer,
    id_companhia integer,
    id_preco text,
    data_ida text,
    data_volta text, 
    assento text,
    portao_embarque text,
    classe text
    );
''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS viajante (
        id integer PRIMARY KEY, 
        nome_viajante text,
        numero_embarque text,
        origem text,
        destino text,
        idade integer
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS companhia_aerea (
        id integer PRIMARY KEY,
        nome_da_empresa TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classe (
        id_classe integer PRIMARY KEY,
        classe text
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS preco (
        id integer PRIMARY KEY,
        preco_da_passagem text,
        tipo text           
        );
    ''')

    conn.commit()

    conn.close()
