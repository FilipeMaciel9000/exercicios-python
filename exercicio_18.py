# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

# Leitura do ângulo
angulo = float(input("Digite o valor do ângulo em graus: "))

# Convertendo o ângulo para radianos
angulo_rad = math.radians(angulo)

# Cálculo do seno, cosseno e tangente
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

# Exibição dos resultados
print(f"O valor do seno de {angulo}° é: {seno:.2f}")
print(f"O valor do cosseno de {angulo}° é: {cosseno:.2f}")
print(f"O valor da tangente de {angulo}° é: {tangente:.2f}")
