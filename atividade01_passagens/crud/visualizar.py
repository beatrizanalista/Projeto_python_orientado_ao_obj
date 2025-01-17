import sqlite3
from prettytable import PrettyTable


def visualizar(tabela):
    conn = sqlite3.connect(
        "..\\banco_de_dados_relacional\\atividade01_passagens\\viajem.db")
    cursor = conn.cursor()

    if tabela == "viajante":
        cursor.execute("Select * FROM viajante")
        resultados = cursor.fetchall()

        # os.system('cls')
        for row in resultados:
            print(row)
        conn.close()

    if tabela == "passagem":
        cursor.execute("SELECT * FROM passagem")
        resultados = cursor.fetchall()

        # os.system('cls')
        for row in resultados:
            print(row)
        conn.close()

    if tabela == "classe":
        cursor.execute("SELECT * FROM classe")
        resultados = cursor.fetchall()

        # os.system('cls')
        for row in resultados:
            print(row)
        conn.close()

    if tabela == "preco":
        cursor.execute("SELECT * FROM preco")
        resultados = cursor.fetchall()

        # os.system('cls')
        for row in resultados:
            print(row)
        conn.close()

    if tabela == "companhia aerea":
        cursor.execute("SELECT * FROM companhia_aerea")
        resultados = cursor.fetchall()

        tabela = PrettyTable()

        colunas = [descricao[0] for descricao in cursor.description]

        tabela.field_names = colunas

        for row in resultados:
            tabela.add_row(row)
    
    
        print(tabela)

        conn.close()
