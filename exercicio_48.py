# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
# Inicializa a soma
soma = 0

# Loop para percorrer todos os números de 1 a 500
for i in range(1, 501):
    if i % 3 == 0:  # Verifica se o número é múltiplo de 3
        soma += i  # Adiciona o múltiplo de 3 à soma

# Exibe o resultado
print(f'A soma de todos os múltiplos de 3 no intervalo de 1 até 500 é: {soma}')
