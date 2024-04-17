import random

def gerar_numero_unico():
    # Gerar um número aleatório de 6 dígitos
    numero_aleatorio = random.randint(100, 999)
               
    # Retornar o número aleatório como uma string
    return str(numero_aleatorio)
