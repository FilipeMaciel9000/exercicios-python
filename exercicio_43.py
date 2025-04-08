# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
# Solicitar o peso e a altura da pessoa
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

# Calcular o IMC
imc = peso / (altura ** 2)

# Exibir o status de acordo com o IMC
if imc < 18.5:
    print(f"IMC = {imc:.2f}: Abaixo do Peso")
elif 18.5 <= imc < 25:
    print(f"IMC = {imc:.2f}: Peso Ideal")
elif 25 <= imc < 30:
    print(f"IMC = {imc:.2f}: Sobrepeso")
elif 30 <= imc < 40:
    print(f"IMC = {imc:.2f}: Obesidade")
else:
    print(f"IMC = {imc:.2f}: Obesidade Mórbida")
