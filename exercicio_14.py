# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = (celsius * 9/5) + 32
print(f'{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F')
