# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
import math

# Leitura dos catetos
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Cálculo da hipotenusa usando o Teorema de Pitágoras
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

# Exibição do resultado
print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")
