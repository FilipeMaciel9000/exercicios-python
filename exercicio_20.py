#  O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#  Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

# Leitura dos nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Lista com os nomes dos alunos
alunos = [aluno1, aluno2, aluno3, aluno4]

# Sorteando a ordem dos alunos
random.shuffle(alunos)

# Exibição da ordem sorteada
print("A ordem sorteada para a apresentação dos trabalhos é:")
for i, aluno in enumerate(alunos, 1):
    print(f"{i}º: {aluno}")
