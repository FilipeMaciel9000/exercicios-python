# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
# Inicialização das variáveis
maiores_18 = 0
homens = 0
mulheres_menor_20 = 0

while True:
    # Leitura dos dados da pessoa
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").strip().lower()

    # Atualização das estatísticas
    if idade > 18:
        maiores_18 += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres_menor_20 += 1

    # Pergunta se o usuário quer continuar
    continuar = input("Deseja continuar cadastrando pessoas? (s/n): ").strip().lower()

    if continuar == 'n':
        break

# Exibição dos resultados
print(f"\nResultados:")
print(f"A) Pessoas com mais de 18 anos: {maiores_18}")
print(f"B) Homens cadastrados: {homens}")
print(f"C) Mulheres com menos de 20 anos: {mulheres_menor_20}")
