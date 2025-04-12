# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# Leitura do número
num = int(input("Digite um número inteiro: "))

# Verifica se o número é menor ou igual a 1
if num <= 1:
    print(f"O número {num} não é primo.")
else:
    # Verificando se o número é primo
    for i in range(2, num):
        if num % i == 0:  # Se o número for divisível por i
            print(f"O número {num} não é primo.")
            break
    else:
        print(f"O número {num} é primo.")
