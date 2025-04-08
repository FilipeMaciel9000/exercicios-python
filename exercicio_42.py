# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes
# Solicitar os comprimentos dos três lados
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Verificar se os lados formam um triângulo
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    print("Os lados podem formar um triângulo!")

    # Determinar o tipo de triângulo
    if lado1 == lado2 == lado3:
        print("Tipo do triângulo: EQUILÁTERO (todos os lados iguais)")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Tipo do triângulo: ISÓSCELES (dois lados iguais, um diferente)")
    else:
        print("Tipo do triângulo: ESCALENO (todos os lados diferentes)")
else:
    print("Os lados não podem formar um triângulo.")
