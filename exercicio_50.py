# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Inicializa a soma como 0
soma = 0

# Lê seis números e verifica se são pares
for i in range(6):
    numero = int(input(f'Digite o {i + 1}º número: '))

    # Verifica se o número é par
    if numero % 2 == 0:
        soma += numero  # Adiciona o número à soma se for par

# Exibe a soma dos números pares
print(f'A soma dos números pares é: {soma}')
