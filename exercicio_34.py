# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
# Leitura do salário do funcionário
salario = float(input("Digite o salário do funcionário: R$"))

# Verificação e cálculo do aumento
if salario > 1250:
    aumento = salario * 0.10  # Aumento de 10% para salários superiores a R$1250,00
else:
    aumento = salario * 0.15  # Aumento de 15% para salários inferiores ou iguais a R$1250,00

# Exibindo o novo salário e o valor do aumento
novo_salario = salario + aumento
print(f"O aumento será de R${aumento:.2f}.")
print(f"O novo salário será R${novo_salario:.2f}.")
