# Crie um programa que faça o computador jogar Jokenpô com você.
import random


# Função que escolhe a opção do computador
def escolha_computador():
    return random.choice(['pedra', 'papel', 'tesoura'])


# Função principal
def jokenpo():
    print("Vamos jogar Jokenpô!")

    # Solicitar a escolha do jogador
    jogador = input("Escolha entre Pedra, Papel ou Tesoura: ").lower()

    # Verificar se a escolha do jogador é válida
    if jogador not in ['pedra', 'papel', 'tesoura']:
        print("Opção inválida! Escolha entre Pedra, Papel ou Tesoura.")
        return

    # Obter a escolha do computador
    computador = escolha_computador()
    print(f"O computador escolheu: {computador}")

    # Comparar as escolhas e determinar o vencedor
    if jogador == computador:
        print("Empate!")
    elif (jogador == 'pedra' and computador == 'tesoura') or \
            (jogador == 'papel' and computador == 'pedra') or \
            (jogador == 'tesoura' and computador == 'papel'):
        print("Você ganhou!")
    else:
        print("O computador ganhou!")


# Executar o jogo
jokenpo()
