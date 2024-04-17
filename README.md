# Sistema Bancário - Documentação

Este é um sistema bancário simples desenvolvido como parte de um desafio no bootcamp da DIO, agora melhorado e expandido para permitir um gerenciamento mais flexível de contas e usuários, com foco em organização e modularidade.

## Funcionalidades Principais

### Cadastro de Usuários e Contas

- **nova_conta_corrente()**:
  Permite que um usuário crie uma nova conta corrente, associada ao seu CPF. Um usuário pode ter várias contas independentes.

- **cadastrar(usuarios)**:
  Permite o cadastro de novos usuários no sistema, armazenando informações como nome, CPF e suas contas associadas.

### Operações em Contas

- **depositar(saldo, deposito, extrato)**:
  Permite que um usuário deposite dinheiro em uma de suas contas correntes. Atualiza o saldo da conta e registra a transação no extrato.

- **sacar(saldo, saque, extrato, limite, numero_saques)**:
  Permite que um usuário faça um saque em uma de suas contas correntes, respeitando as seguintes regras:
  - Limite de 3 saques por dia.
  - Valor máximo de saque por transação é R$500.
  - Não é possível sacar valores negativos ou superiores ao saldo disponível.

- **operacoes_da_conta(usuario, conta)**:
  Exibe todas as operações realizadas em uma determinada conta de um usuário, incluindo depósitos e saques.

### Consulta e Gerenciamento de Contas

- **mostrar_contas(usuario)**:
  Lista todas as contas associadas a um determinado usuário, identificado pelo CPF.

## Orientações Futuras

Para o futuro irei implementar ao sistema: POO


## Uso e Contribuições

Para utilizar este sistema bancário, basta clonar o repositório e executar o código Python localmente. Certifique-se de ter o Python instalado em seu ambiente.


## Autor

Este sistema foi desenvolvido por Emanuelle Gonçalo como parte do bootcamp da DIO. 