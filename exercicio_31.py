# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
# Leitura da distância da viagem
distancia = float(input("Digite a distância da viagem em Km: "))

# Calcular o preço da passagem
if distancia <= 200:
    preco = distancia * 0.50  # R$0,50 por Km para viagens de até 200Km
else:
    preco = distancia * 0.45  # R$0,45 por Km para viagens acima de 200Km

# Exibir o preço da passagem
print(f"O preço da passagem é R${preco:.2f}.")
