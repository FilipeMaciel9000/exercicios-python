# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
# Leitura do primeiro termo e da razão
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicialização das variáveis
termo = primeiro_termo
contador = 0

# Loop para mostrar os termos
while True:
    # Pergunta quantos termos deseja mostrar
    termos_a_mostrar = int(input("Quantos termos você quer mostrar? (Digite 0 para encerrar): "))

    if termos_a_mostrar == 0:
        print("Programa encerrado.")
        break

    # Exibindo os próximos termos
    for _ in range(termos_a_mostrar):
        print(termo, end=" ")
        termo += razao
        contador += 1

    print()  # Nova linha para separar os conjuntos de termos
