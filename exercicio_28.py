# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

# O computador "pensa" em um número entre 0 e 5
numero_computador = random.randint(0, 5)

# O usuário tenta adivinhar o número
numero_usuario = int(input("Tente adivinhar o número que o computador escolheu (entre 0 e 5): "))

# Verificando se o usuário acertou
if numero_usuario == numero_computador:
    print("Parabéns! Você acertou o número!")
else:
    print(f"Você errou. O número que o computador escolheu era {numero_computador}.")
