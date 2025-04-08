# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário atual do funcionário (R$): '))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f'Salário atual: R$ {salario:.2f}')
print(f'Aumento de 15%: R$ {aumento:.2f}')
print(f'Novo salário: R$ {novo_salario:.2f}')
