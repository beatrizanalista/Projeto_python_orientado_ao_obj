from apagar import apagar
from visualizar import visualizar
from atualizar import atualizar
from adicionar import adicionar
import os

Sub_menu = ['passagem','viajante','preco','classe','companhia aerea']

while True:
    os.system('cls')
    print("\n=== Sistema de Passagens Aéreas ===")
    print("1. Cadastrar informações para a compra")
    print("2. Consultar passagem")
    print("3. Atualizar as Informações")
    print("4. Excluir informação do resgistro da passagem")
    print("5. Sair do site")
    opcao = input("Aperte uma opção: ")

    if opcao == '1':
        os.system('cls')
        for item in Sub_menu:
            print(item, end=' | ') 
        pergunta = input("\nEm  qual tabela você deseja adicionar informações: ")
        adicionar(pergunta)
    elif opcao == '2':
        os.system('cls')
        for item in Sub_menu:
            print(item, end=' | ') 
        pergunta = input("Escolha uma tabela para vizualizar: ")
        visualizar(pergunta)
        input('Pressione ENTER para voltar: ')
    elif opcao == '3':
        os.system('cls')
        for item in Sub_menu:
            print(item, end=' | ') 
        pergunta = input("Escolha uma tabela você deseja atualizar: ")
        atualizar(pergunta)
    elif opcao == '4':
        os.system('cls')
        for item in Sub_menu:
            print(item, end=' | ') 
        pergunta = input("Em qual tabela você deseja apagar: ")
        apagar(pergunta)
    elif opcao == '5':
        os.system('cls')
        print("Obrigado, boa viajem!")
        break
    else:
        print()
