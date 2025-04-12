# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
# Inicializando as variáveis para armazenar os pesos
maior_peso = float('-inf')  # Inicializa com um valor muito baixo
menor_peso = float('inf')  # Inicializa com um valor muito alto

# Laço para ler os pesos de 5 pessoas
for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa (em kg): "))

    # Verifica se o peso é o maior
    if peso > maior_peso:
        maior_peso = peso

    # Verifica se o peso é o menor
    if peso < menor_peso:
        menor_peso = peso

# Exibe os resultados
print(f"\nO maior peso é: {maior_peso} kg")
print(f"O menor peso é: {menor_peso} kg")
