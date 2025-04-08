# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto (R$): '))
desconto = preco * 0.05  # 5% do preço
novo_preco = preco - desconto  # Aplica o desconto

# Exibição formatada
print(f'Preço original: R$ {preco:.2f}')
print(f'Desconto de 5%: R$ {desconto:.2f}')
print(f'Preço com desconto: R$ {novo_preco:.2f}')
