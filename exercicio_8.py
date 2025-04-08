#  Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

me = float(input('Insira o valor que será convertido em metros: '))
c = me * 100
mi = me * 1000
print(f'{me:.2f} metros corresponde a {c:.2f} centimetros e a {mi:.2f} milimetros')
