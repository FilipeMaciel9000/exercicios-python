# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
# Leitura do valor a ser sacado
valor_sacado = int(input("Digite o valor a ser sacado: R$ "))

# Definindo as cédulas disponíveis
cedulas = [50, 20, 10, 1]

# Inicializando a contagem de cédulas
for cedula in cedulas:
    quantidade_cedulas = valor_sacado // cedula  # Quantidade de cédulas de determinado valor
    if quantidade_cedulas > 0:
        print(f"Cédulas de R${cedula}: {quantidade_cedulas}")
    valor_sacado %= cedula  # Atualiza o valor a ser sacado após a retirada das cédulas
