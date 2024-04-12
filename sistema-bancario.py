menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

deposito = 0

while True:
    opcao = input(menu)
    
    #DEPOSITO
    if opcao == "d":
        deposito = float(input("Infome o valor a ser depositado: "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R${deposito:.2f}\n"
            print(f"R${saldo:.2f} depositado.")
        else:
            print("Insira um valor válido para depósito.")
    
    #SAQUE
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES and saldo > 0:
        
                saque = float(input("Informe o valor do saque: "))

                if saque > 0 and saque <= saldo and saque <= 500:
                    saldo -= saque
                    extrato += f"Saque: R${saque:.2f}\n"
                    numero_saques += 1
                    print(f"Saque de R${saque:.2f} realizado.") 

                elif saldo < saque:
                    print("Saldo insuficiente.")

                else:
                    mensagem = "Limite de saque excedido." if saque > 500 else "Informe um valor válido."
                    print(mensagem)
                
        else:
            mensagem = "Número de saques excedido." if numero_saques >= LIMITE_SAQUES else "Saldo insuficiente."  
            print(mensagem)

    #EXTRATO
    elif opcao == "e":
        print(f"{extrato}\nTotal disponível: R${saldo:.2f}.")

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")