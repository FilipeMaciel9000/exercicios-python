# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Leitura do número
numero = input("Digite um número de 0 a 9999: ")

# Garantir que o número tenha 4 dígitos, preenchendo com zeros à esquerda se necessário
numero = numero.zfill(4)

# Exibir cada dígito separado
print(f"Unidade: {numero[3]}")
print(f"Dezena: {numero[2]}")
print(f"Centena: {numero[1]}")
print(f"Milhar: {numero[0]}")
