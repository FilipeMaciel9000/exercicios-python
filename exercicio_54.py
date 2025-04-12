# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date

# Inicializa as contagens
menores_idade = 0
maiores_idade = 0

# Pergunta o ano de nascimento de 7 pessoas
for i in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    idade = date.today().year - ano_nascimento  # Calcula a idade da pessoa

    if idade < 18:
        menores_idade += 1
    else:
        maiores_idade += 1

# Exibe os resultados
print(f"\nPessoas que não atingiram a maioridade: {menores_idade}")
print(f"Pessoas que já são maiores de idade: {maiores_idade}")
