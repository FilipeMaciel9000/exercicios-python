# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

# Leitura dos nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Lista com os nomes dos alunos
alunos = [aluno1, aluno2, aluno3, aluno4]

# Sorteio de um aluno
escolhido = random.choice(alunos)

# Exibição do nome do aluno sorteado
print(f"O aluno sorteado para apagar o quadro é: {escolhido}")
