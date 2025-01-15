import sqlite3 
from prettytable import PrettyTable
from pathlib import Path
import os


os.system('cls')


db_path = path('BD') / 'bd_rel_1_n_.db'
conn = sqlite3.connect(str(db_path))
cursor = conn.cursor()

# Criação da tabela 'clientes' (tabela principal)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT, -- ID unico para o cliente
    nome TEXT NOT NULL,                           -- Nome do cliente
    email TEXT UNIQUE NOT NULL,                   -- email unico
    telefone TEXT,                                 -- Telefone do cliente
    cidade TEXT                                    -- cidade onde mora
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT, -- ID unico para o pedido
    id_cliente INTEGER NOT NULL,                 -- Relacionamento com a tabela Clientes
    produto TEXT NOT NULL,                        -- Nome do produto pedido
    quantidade INTEGER NOT NULL,                  -- Quantidade do produto
    data TEXT NOT NULL,                           -- Data do pedido
    valor_total REAL NOT NULL,                     -- Valor total do pedido
    FOREIGN KEY (id_cliente) REFERENCES Clientes (id_cliente) -- Chave estrangeira
)
''')


def cliente_existe(id_cliente):
    cursor.execute(
        'SELECT 1 FROM Clientes WHERE id_clientes = ?', (id_cliente,))
    return cursor.fetchone() is not None



def inserir_cliente():
    nome = input('Digite o nome do cliente: ')
    email = input('Digite o email do cliente: ')
    telefone = input('Digite Digite o telefone do cliente: ')
    cidade = input('Digite a cidade do cliente: ')
    cursor.execute('''
    INSERT INTO Clientes (nome, email, telefone, cidade)
    VALUES (?, ?, ?, ?)
    ''', (nome, email, telefone, cidade))
    conn.commit()
    print('Cliente inserido com sucesso!')



def inserir_pedido():
    cursor.execute('''
    SELECT * from clientes
    ''')
    resultados = cursor.fetchall()

    if not resultados:
        print('-'*70)
        print('Nenhum cliente encontrado. Cadastre um cliente primeiro.')
        print('-' * 70)
        return
    
    tabela = PrettyTable(['id_cliente', 'None', 'Email', 'Telefone', 'Cidade'])
    for linha in resultados:
        tabela.add_row(linha)
    print(tabela)

    try:
        id_cliente = int(input('Digite o ID do cliente: '))

        if not cliente_existe(id_cliente):
            print('-'*70)
            print(f'Erro: Cliente com ID {id_cliente} não encontrado!')
            print('Por favor, cadastre o cliente primeiro.')
            print('-'*70)
            
            return

        produto = input('Digite o nome do produto: ')
        quantidade = int(input('Digite a quantidade:'))

        data = input('Digite a data do pedido (yyyy-MM-DD): ')
        valor_total = float(input('Digite o valor total: '))

        cursor.execute('''
        INSERT INTO pedidos (id_cliente, produto, quantidade, data, valor_total)
        VALUES (?, ?, ?, ?, ?)
        ''', (id_cliente, produto, quantidade, data, valor_total))
        conn.commit()
        print('Pedido inserido com sucesso!')
    except ValueError:
        print('-'*70)
        print('Erro: ID do cliente deve ser um número inteiro.')
        print('-'*70)


def consultar_pedidos():
    cursor.execute('''
    SELECT
        clientes.nome, Clientes.email, Clientes.cidade, -- campos da tabela clientes
        Pedidos.pedido, Pedido.quantidade, Pedidos.valor_total -- campos da tabela pedidos
    FROM
        Clientes
    JOIN
        pedidos ON Clientes.id_cliente = Pedido.id_cliente
    ''')
    resultados = cursor.fetchall()

    tabela = PrettyTable(
        ['None', 'Email', 'cidade', 'produto', 'quantidade', 'valor total'])
    for linha in resultados:
        tabela.add_row(linha)
    print(tabela)

def alterar_pedido():
    try:
        id_pedido = int(input('Digite o ID do pedido que deseja alterar: '))

        cursor.execute(
            'SELECT * FROM pedidos WHERE id_peido = ?', (id_pedido))
        pedido = cursor.fetchone()
        
        if not pedido:
            print('-'*70)
            print(f'Erro: Pedido com ID {id_pedido} não encontrado!')
            print('-' * 70)
            return
        
        print('-' * 70)
        print('Dados atuais do pedido:')
        print(f'Produto; {pedido[2]}')
        print(f'Quantidade: {pedido[3]}')
        print(f'Data: {pedido[4]}')
        print(f'Valor Total: {pedido[5]}')
        print('-' *70)

        produto = input(
            'Digite o novo nome do produto (ou pressione Enter para manter o atual): ') or pedido[2]
        quantidade = input(
            'Digite a nova quantidade (ou pressione Enter para manter a atual): ') or pedido[3]
        data = input(
            'Digite a nova data (yyyy-MM-DD) (ou pressione Enter para manter a atual): ') or pedido[4]
        valor_total = input(
            'Digite o novo valor total (ou pressione Enter para manter o atual): ') or pedido[5]
        

        cursor.execute('''
        UPDATE Pedidos
        SET produto = ?, quantidade = ?, data = ?, valor_total = ?
        WHERE  id_pedido = ?
        ''', (produto, int(quantidade), data, float(valor_total), id_pedido))
        conn.commit()
        print('Pedido atualizado com sucesso!')
    except ValueError:
        print('-'*70)
        print('Erro: Entrada invalida')
        print('-' *70)