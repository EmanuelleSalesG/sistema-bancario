# Sistema Bancário Bootcamp DIO
Este é um sistema bancário simples desenvolvido como parte de um desafio no bootcamp da DIO (Digital Innovation One). Ele possui as seguintes funcionalidades:

* Depósito: Permite ao usuário realizar um depósito na conta bancária.
* Saque: Permite ao usuário fazer um saque da conta, respeitando as seguintes regras:
* Limite de 3 saques por dia.
* Valor máximo de saque por transação é R$500.
* Não é possível sacar valores negativos ou superiores ao saldo disponível.
* Extrato: Exibe o saldo atual da conta.
* Sair: Encerra o programa.

## Este sistema foi otimizado e testado para garantir que atenda às regras especificadas:

* Limitação de Saques: A cada dia, o usuário só pode realizar até 3 saques.
* Valor Máximo de Saque: Cada transação de saque tem um limite máximo de R$500.
* Validação de Entradas:
* Não são permitidos saques de valores negativos.
* Depósitos também não aceitam valores negativos.
