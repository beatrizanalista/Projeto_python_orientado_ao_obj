import os
import sqlite3
os.system('cls')

conn = sqlite3.connect(
    "C:/repositorio_beatriz/banco_de_dados_relacional/atividade01_passagens/viajem.db")

cursor = conn.cursor()


def adicionar_passagem():
    passagem =  [(2, 2, 3, 4, 5, '11-08-2025', '13-08-2025', '05B', 7, 'Classe Executiva'),
                (3, 3, 4, 5, 6, '03-03-2025', '02-04-2026', '30D', 14, 'Primeira Classe'),
                (4, 4, 5, 6, 7, '10-11-2024', '01-02-2025', '20C', 12, 'classe Execultiva'),
                (5, 5, 6, 7, 8, '06-10-2025', '14-11-2025', '06B', 13, 'classe Economica'),
                (6, 6, 7, 8, 9, '23-12-2024', '20-01-2025', '23A', 16, 'Primeira Classe')]
    cursor.executemany(
        'INSERT INTO passagem (id,id_viajante,id_cadeira,id_companhia,id_preco, data_ida,data_volta, assento,portao_embarque, classe ) values  (?,?,?,?,?,?,?,?,?,?)', passagem)
 
    viajante = [('Henrique', 'JJ1234', 'França','Belgica', 32),
                ('cleber', 'LL2345', 'Estados Unidos', 'Espanha', 23),
                ('Rafael', 'AA3456', 'Holanda','China', 44),
                ('Luiza', 'BB4567', 'Japao', 'Suica', 50),
                ('Rodrigo', 'CC5678', 'Canada', 'Argentina', 18),
                ('Pedro', 'QQ6789', 'Brasil', 'Chile', 65)]
    cursor.executemany(
        ' INSERT INTO viajante (nome_viajante ,numero_embarque,origem ,destino,idade) values (?,?,?,?,?)', viajante)


    companhia_aerea = [(1, 'American Airlines'),
                       (2, 'LATAM Airlines'),
                       (3, 'Azul Linhas Aéreas'),
                       (4, 'Air France'),
                       (5, 'United Airlines'),
                       (6, 'Airlines Argentina')]
    cursor.executemany(
        ' INSERT INTO companhia_aerea (id,nome_da_empresa) values (?,?) ', companhia_aerea)

    classe = [(1, 'classe economica'),
              (2, 'primeira classe'),
              (3, 'classe executiva')]
    cursor.executemany(' INSERT INTO classe (id_classe, classe) values(?,?)', classe)
   
    preco = [(1, 18.000, 'primeira_classe'),
             (2, 2.500, 'classe executiva'),
             (3, 1.000, 'classe economica')]
    cursor.executemany(
        ' INSERT INTO preco (id,preco_da_passagem,tipo) values (?,?,?)', preco)

    conn.commit()
    conn.close()

# adicionar_passagem()

print("passagem feita!")
