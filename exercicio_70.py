# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
# Inicialização das variáveis
total_gasto = 0
produtos_acima_1000 = 0
menor_preco = float('inf')  # Inicializa com um valor infinito para garantir que qualquer preço será menor
produto_mais_barato = ""

while True:
    # Leitura do nome e preço do produto
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$ "))

    # Atualiza o total gasto
    total_gasto += preco

    # Conta quantos produtos custam mais de R$1000
    if preco > 1000:
        produtos_acima_1000 += 1

    # Verifica qual é o produto mais barato
    if preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = nome

    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja continuar cadastrando produtos? (s/n): ").strip().lower()

    if continuar == 'n':
        break

# Exibição dos resultados
print(f"\nResultados:")
print(f"A) Total gasto na compra: R$ {total_gasto:.2f}")
print(f"B) Quantidade de produtos que custam mais de R$1000: {produtos_acima_1000}")
print(f"C) Produto mais barato: {produto_mais_barato} (R$ {menor_preco:.2f})")
