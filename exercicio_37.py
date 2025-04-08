#  Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
# Solicitar o número inteiro
numero = int(input("Digite um número inteiro: "))

# Solicitar a base de conversão
print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
base = int(input("Digite sua opção (1/2/3): "))

# Converter o número para a base escolhida
if base == 1:
    print(f"O número {numero} em binário é: {bin(numero)[2:]}")
elif base == 2:
    print(f"O número {numero} em octal é: {oct(numero)[2:]}")
elif base == 3:
    print(f"O número {numero} em hexadecimal é: {hex(numero)[2:]}")
else:
    print("Opção inválida! Por favor, escolha 1, 2 ou 3.")
