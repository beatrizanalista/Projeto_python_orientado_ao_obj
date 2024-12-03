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

conn = sqlite3.connect("c:/repositorios/banco_de_dados_relacional/meu_banco.db")

cursor = conn.cursor()

def criando_bd():
    sqlite3.cursor('''CREATE TABLE passagem (
    'id_bilhete'int,
    'nome_viajante'int,
    'id_cadeira'int,
    'id_preco'decimal,
    'direto_ou_escala'into,
    'ida_volta'int,
    'ida'int,
    'data'int,
    'hora'float,
    'Assento',
    'portao_emparque'int,
    'destino'int,
    'classe de Assento',
    ''');
def criando_bd():
    sqlite3('''CREATE TABLE escala (
    'id,int'
    'data,float',
    'hora,decimal',
    'portao_embarque,int',
    'companhia aerea'int',
    'local_embarque,int',
    ''');

def criando_bd():
    sqlite3('''CREATE TABLE viajante (
    'id,int',
     ''' );
    
def criando_bd():
    sqlite3('''CREATE TABLE empresa (
    'gol Ailines',
    'Latam Airlines',
    'Azul linhas Aereas',
    'American Airlines',
    'Air france',
    'Qatar airways'
    ''');
    
def criando_bd():
    sqlite3(''' CREATE TABLE classe(
        ''');

def criando_bd():
    sqlite3(''' CREATE TABLE preco (
        ''');
    
   