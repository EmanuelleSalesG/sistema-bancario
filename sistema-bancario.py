from operacoes_conta import *

usuario_login = """
============ BANK DIO BOOTCAMP ============
[1] Criar conta
[2] Conta Corrente
[q] Sair
==> """

usuarios = []

while True:
    opcao = input(usuario_login)

    if opcao == '1':
        print("============ CADASTRO ============")
        cadastrar(usuarios)

    elif opcao == '2':
        print("============ BUSCAR USUÁRIO ============")
        cpf =  input("CPF (Apenas números): ")
        numero_conta = input("Número da conta: ")
        usuario_encontrado = False

        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                for conta in usuario["contas"]:
                    if conta["numero_conta"] == numero_conta:
                       operacoes_da_conta(usuario, conta)
                       usuario_encontrado = True
        
        if not usuario_encontrado:
            print("\nErro! Conta não encontrada")

    elif opcao == 'q':
        break;

    else:
        print("Opção inválida.")