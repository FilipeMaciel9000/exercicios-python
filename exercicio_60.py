# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# Leitura do número
num = int(input("Digite um número para calcular seu fatorial: "))

# Inicialização do fatorial
fatorial = 1

# Calculando o fatorial
for i in range(1, num + 1):
    fatorial *= i

# Exibindo o resultado
print(f"O fatorial de {num} é {fatorial}")
