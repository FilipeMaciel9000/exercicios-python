# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo
while True:
    # Leitura do número
    numero = int(input("Digite um número para ver sua tabuada (número negativo para parar): "))

    # Condição de parada
    if numero < 0:
        print("Programa encerrado.")
        break

    # Exibindo a tabuada do número
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print("-" * 20)  # Linha para separar as tabuadas
