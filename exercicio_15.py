# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar.
# Sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram percorridos? '))

preco_por_dia = 60
preco_por_km = 0.15

total = (dias * preco_por_dia) + (km * preco_por_km)

print(f'O total a pagar pelo aluguel do carro é: R$ {total:.2f}')
