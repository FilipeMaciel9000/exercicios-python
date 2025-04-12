# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

# Inicialização da variável de vitórias consecutivas
vitorias_consecutivas = 0

while True:
    # Leitura da escolha do jogador
    jogador = int(input("Escolha um número: "))
    escolha = input("Par ou Ímpar? (P/I): ").strip().lower()

    # Validação da escolha (par ou ímpar)
    if escolha not in ['p', 'i']:
        print("Opção inválida. Escolha 'P' para Par ou 'I' para Ímpar.")
        continue

    # O computador escolhe um número aleatório
    computador = random.randint(0, 10)
    total = jogador + computador

    # Verificar se o total é par ou ímpar
    if total % 2 == 0:
        resultado = 'p'  # Par
    else:
        resultado = 'i'  # Ímpar

    print(f"Você jogou {jogador} e o computador jogou {computador}. Total: {total}.")

    # Verificar se o jogador venceu
    if resultado == escolha:
        print("Você venceu!")
        vitorias_consecutivas += 1
    else:
        print(f"Você perdeu! Total de vitórias consecutivas: {vitorias_consecutivas}")
        break
