#  Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um número: '))
print(f'Tabuada de {n}:')
for i in range(1, 11):
    print(f'{n} * {i} = {i*n}')
