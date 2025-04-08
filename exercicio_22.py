# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.
from nameparser import HumanName

# Leitura do nome completo
nome_completo = input("Digite o seu nome completo: ")

# Usando o nameparser para separar o nome
nome = HumanName(nome_completo)

# Nome em maiúsculas e minúsculas
nome_maiusculas = nome_completo.upper()
nome_minusculas = nome_completo.lower()

# Quantidade total de letras (sem considerar espaços)
quantidade_letras = len(nome_completo.replace(" ", ""))

# Quantidade de letras do primeiro nome
quantidade_primeiro_nome = len(nome.first)

# Exibindo os resultados
print(f"O nome em maiúsculas: {nome_maiusculas}")
print(f"O nome em minúsculas: {nome_minusculas}")
print(f"Quantidade total de letras (sem considerar espaços): {quantidade_letras}")
print(f"Quantidade de letras do primeiro nome: {quantidade_primeiro_nome}")
