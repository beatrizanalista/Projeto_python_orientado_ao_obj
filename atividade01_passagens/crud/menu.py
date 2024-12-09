from apagar import apagar
import os



while True:
    os.system("cls")
    print("\n=== Sistema de Passagens Aéreas ===")
    print("1. Criar conta")
    print("2. Cadastrar imformações para a compra")
    print("3. Consultar passagem")
    print("5. Atualizar as Informações")
    print("6. Excluir informação do resgistro da passagem")
    print("7. Sair do site")
    opcao = input("Aperte uma opção: ")

    if opcao == '1':
        pass
    elif opcao == '2':
        pass
    elif opcao == '3':
        pass
    elif opcao == '4':
        pass
    elif opcao == '5':
        pass
    elif opcao == '6':
       pergunta = input("Em qual tabela você deseja apagar? ")
       apagar(pergunta)
    elif opcao == '7':
        print("Obrigado, boa viajem!")
        break
    else:
        print("Ops...ocorreu um erro,tente novamente.")