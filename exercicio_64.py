# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# Inicialização das variáveis
contador = 0
soma = 0

while True:
    # Leitura do número
    numero = int(input("Digite um número (ou 999 para parar): "))

    # Condição de parada
    if numero == 999:
        break

    # Atualiza o contador e a soma
    contador += 1
    soma += numero

# Exibe o resultado
print(f"Você digitou {contador} números.")
print(f"A soma entre os números digitados é {soma}.")
