def adicionar_passagem(id,id_viajante,id_cadeira,id_companhia,id_preco, data_ida,data_volta, assento,portao_embarque, classe )
cursor.execute('''
    INSERT INTO passagem (id,id_viajante,id_cadeira,id_companhia,id_preco, data_ida,data_volta, assento,portao_embarque, classe )
    values (1,1,2,3,4,03/08/2025,17/02/2025,17E,23,Classe Econômica)
            (2,2,3,4,5,11/08/2025,13/08/2025,05B,7,Classe Executiva)
            (3,3,4,5,6,03/03/2025,02/04/2026,30D,14,Primeira Classe)
     ''')
conn.commit()
    
 print("passagem feita!")         