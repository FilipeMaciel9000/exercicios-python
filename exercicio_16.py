#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
numero = float(input('Digite um número: '))
print(f'A parte inteira de {numero} é {trunc(numero)}')