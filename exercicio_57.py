# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
# Laço para garantir que o valor seja válido
while True:
    sexo = input("Digite o sexo (M para masculino ou F para feminino): ").strip().upper()

    # Verifica se o valor é válido
    if sexo == 'M' or sexo == 'F':
        print(f"Sexo {sexo} registrado com sucesso!")
        break
    else:
        print("Valor inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")
