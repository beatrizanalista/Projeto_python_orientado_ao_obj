from apagar import apagar
from visualizar import visualizar
from atualizar import atualizar
from adicionar import adicionar
import os


while True:
    os.system("cls")
    print("\n=== Sistema de Passagens Aéreas ===")
    print("1. Cadastrar imformações para a compra")
    print("2. Consultar passagem")
    print("3. Atualizar as Informações")
    print("4. Excluir informação do resgistro da passagem")
    print("5. Sair do site")
    opcao = input("Aperte uma opção: ")

    if opcao == '1':
        pergunta = input("cadastre informações para a compra da passagem:")
        adicionar(pergunta)
    elif opcao == '2':
        pergunta = input("Em qual tabela você deseja visualizar:")
        visualizar(pergunta)
        input('Presione enter pra voltar:')
    elif opcao == '3':
        pergunta = input("Em qual tabela você deseja atualizar?")
        atualizar(pergunta)
    elif opcao == '4':
        pergunta = input("Em qual tabela você deseja apagar? ")
        apagar(pergunta)
    elif opcao == '5':
        print("Obrigado, boa viajem!")
        break
    else:
        print("Ops...ocorreu um erro,tente novamente.")
