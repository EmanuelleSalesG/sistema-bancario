from numero_conta import gerar_numero_unico

def nova_conta_correte():
    numero = gerar_numero_unico()
    nova_conta = {"numero_conta": numero, "agencia": "0001", "saldo": 0.0, "extrato": ""}
    
    print("\nNova conta criada com sucesso!\n")
    print(f"Agência: {nova_conta['agencia']}\nConta: {nova_conta['numero_conta']}\n")

    return nova_conta

def cadastrar(usuarios):
    #solicitando dados
    cpf = input("CPF: ")
    check = False
    

    for usuario in usuarios:
        if(usuario["cpf"] == cpf):
            check = True
                    
            
    if check:
        nova_conta = nova_conta_correte()
        usuario["contas"].append(nova_conta)
        
    else:
        numero_conta = gerar_numero_unico()
        usuarios.append({"nome": input("Nome: "), 
            "data_nascimento": input("Data de Nascimento(DD/MM/AAAA): "), 
            "cpf": cpf,
            "endereco": {
            "rua": input("Rua:"), 
            "numero": input("Número:"), 
            "bairro": input("Bairro:"), 
            "cidade": input("Cidade:"), 
            "estado": input("Estado:")
            },
            "contas": [
                {"numero_conta": numero_conta, "agencia":"0001", "saldo": 0.0, "extrato": " "}
            ]   
        })
        print("\nUsuário cadastrado com sucesso!\n")
        print(f"Agência: {usuarios[-1]['contas'][0]['agencia']}\nConta: {usuarios[-1]['contas'][0]['numero_conta']}\n")

    
    return usuarios

def depositar(saldo, deposito, extrato, /): 
    
    if deposito > 0:
        saldo += deposito
        extrato += f"Deposito: R${deposito:.2f}\n"
        print(f"R${saldo:.2f} depositado.")
    else:
        print("Insira um valor válido para depósito.\n")
    
    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques):   
    
        if saque > 0 and saque <= saldo and saque <= limite:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1
            print(f"Saque de R${saque:.2f} realizado.") 

        elif saldo < saque:
            print("Saldo insuficiente.")

        else:
            mensagem = "Limite de saque excedido." if saque > limite else "Informe um valor válido."
            print(mensagem)
        
        return saldo, extrato

def operacoes_da_conta(usuario, conta):
    
    LIMITE_SAQUES = 3
    deposito = 0
    numero_saques = 0
    limite = 500

    menu = """
============ TRANSAÇÃO DESEJADA ============
[d] Depositar
[s] Sacar
[e] Extrato
[m] Exibir contas
[q] Sair
=> """

    
    
    while True:
        opcao = input(menu)
        
        #DEPOSITO
        if opcao == "d":
            
            deposito = float(input("Infome o valor a ser depositado: "))
            if deposito > 0:
                conta["saldo"], conta["extrato"] = depositar(conta["saldo"], deposito, conta["extrato"])

        #SAQUE
        elif opcao == "s":

            if numero_saques < LIMITE_SAQUES and conta["saldo"] > 0:

                saque = float(input("Informe o valor do saque: "))
                numero_saques += 1

                conta["saldo"], conta["extrato"] = sacar(saldo=conta["saldo"], saque=saque, extrato=conta["extrato"], limite=limite, numero_saques=numero_saques)

            else:
                mensagem = "Número de saques excedido." if numero_saques >= LIMITE_SAQUES else "Saldo insuficiente."  
                print(mensagem)

        #EXTRATO
        elif opcao == "e":
            print(f"{conta['extrato']}\nTotal disponível: R${conta['saldo']:.2f}.")
        
        elif opcao == "m":
            mostrar_contas(usuario)

        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


def mostrar_contas(usuario):
    for conta in usuario["contas"]:
        print(f"\nAgencia:{conta['agencia']}\nConta:{conta['numero_conta']}\nSaldo:{conta['saldo']}\n\n")
        