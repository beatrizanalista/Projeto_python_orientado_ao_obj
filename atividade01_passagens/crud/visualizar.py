import sqlite3


conn = sqlite3.connect(
    "..\\banco_de_dados_relacional\\atividade01_passagens\\viajem.db")
cursor = conn.cursor()


def visualizar(tabela):
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
        
    if tabela == "companhia_aerea":
        cursor.execute("SELECT * FROM companhia_aerea")
        resultados = cursor.fetchall()


        # os.system('cls')
        for row in resultados:
            print(row)
        conn.close()
   