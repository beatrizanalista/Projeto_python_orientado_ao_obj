def adicionar_passagem(id,id_viajante,id_cadeira,id_companhia,id_preco, data_ida,data_volta, assento,portao_embarque, classe )
cursor.execute('''
    INSERT INTO passagem (id,id_viajante,id_cadeira,id_companhia,id_preco, data_ida,data_volta, assento,portao_embarque, classe )
    values (1,1,2,3,4,03/08/2025,17/02/2025,17E,23,Classe Econômica),
            (2,2,3,4,5,11/08/2025,13/08/2025,05B,7,Classe Executiva),
            (3,3,4,5,6,03/03/2025,02/04/2026,30D,14,Primeira Classe)
    );
    ''')

def adicionar_viajante(id,nome_viajante ,numero_embarque,origem ,destino,idade)
cursor.execute('''
    INSERT INTO viajante (id,nome_viajante ,numero_embarque,origem ,destino,idade)
    values (2,Henrique,JJ1234,salvador,Feira de Santana,32),
            (3,cleber,LL2345,Porto Alegre ,espirito santo,23),
            (4,Rafael,AA3456,Sao paulo,Estados unidos,44)
);
    ''')        
def adicionar_companhia_aerea (id,nome_da_empresa):
cursor.execute('''
    INSERT INTO companhia_aerea (id,nome_da_empresa)
    values (1,American Airlines),
            (2,LATAM Airlines),
            (3,Azul Linhas Aéreas),
            (4,Air France),
            (5,United Airlines)
''')       
def adicionar_classe (id,classe):
cursor.execute('''
    INSERT INTO classe (id,classe)
    values (1,classe economica),
           (2,primeira classe ),
            (3,classe executiva)
);
''')
def adicionar_preco (id,preco_da_passagem,tipo):
cursor.execute('''
  INSERT INTO preco (id,preco_da_passagem,tipo)
values (1,18.000,primeira_classe),
        (2,2.500,classe executiva),
        (3,1.000,classe economica)
   );
''')
conn.commit()
    
print("passagem feita!")         