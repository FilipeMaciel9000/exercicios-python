# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
# Solicitar os dois números inteiros
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Comparar os números e exibir a mensagem correspondente
if numero1 > numero2:
    print("O primeiro valor é maior.")
elif numero2 > numero1:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior, os dois são iguais.")
