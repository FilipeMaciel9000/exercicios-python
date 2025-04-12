# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa.
# Mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
# Inicializando as variáveis
soma_idades = 0
maior_idade_homem = 0
nome_homem_mais_velho = ""
mulheres_menor_20 = 0

# Laço para ler os dados de 4 pessoas
for i in range(1, 5):
    print(f"Pessoa {i}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().lower()

    # Acumulando a soma das idades para calcular a média
    soma_idades += idade

    # Verificando o homem mais velho
    if sexo == 'm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    # Contando as mulheres com menos de 20 anos
    if sexo == 'f' and idade < 20:
        mulheres_menor_20 += 1

# Calculando a média de idade
media_idades = soma_idades / 4

# Exibindo os resultados
print(f"\nResultados:")
print(f"A) Média de idade do grupo: {media_idades:.2f} anos")
print(f"B) Nome do homem mais velho: {nome_homem_mais_velho}")
print(f"C) Mulheres com menos de 20 anos: {mulheres_menor_20}")
