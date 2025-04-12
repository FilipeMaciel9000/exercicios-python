# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
# Inicialização das variáveis
soma = 0
contador = 0
maior = None
menor = None

while True:
    # Leitura do número
    numero = int(input("Digite um número inteiro: "))

    # Atualizando a soma e o contador
    soma += numero
    contador += 1

    # Atualizando o maior e menor valor
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

    # Pergunta se o usuário quer continuar
    continuar = input("Você quer continuar? (s/n): ").strip().lower()

    # Se a resposta for 'n', o programa termina
    if continuar == 'n':
        break

# Calculando a média
media = soma / contador if contador > 0 else 0

# Exibindo os resultados
print(f"\nVocê digitou {contador} números.")
print(f"A média dos números é {media:.2f}.")
print(f"O maior valor digitado foi {maior}.")
print(f"O menor valor digitado foi {menor}.")
