# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random

# O computador escolhe um número aleatório entre 0 e 10
numero_computador = random.randint(0, 10)

# Inicializa a contagem de palpites
palpites = 0
acertou = False

# O jogador tenta adivinhar o número
print("Bem-vindo ao jogo! Tente adivinhar o número que o computador pensou, entre 0 e 10.")

# Laço para o jogador continuar tentando até acertar
while not acertou:
    # Leitura do palpite do jogador
    palpite = int(input("Digite seu palpite: "))

    # Incrementa o número de palpites
    palpites += 1

    # Verifica se o jogador acertou
    if palpite == numero_computador:
        acertou = True
    else:
        if palpite < numero_computador:
            print("Mais... Tente um número maior!")
        elif palpite > numero_computador:
            print("Menos... Tente um número menor!")

# Quando acertar, mostra o número de palpites
print(f"Parabéns! Você acertou o número {numero_computador} em {palpites} tentativas.")
