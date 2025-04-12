# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# Leitura do primeiro termo e da razão
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicializando a variável para controlar o número de termos
termo = primeiro_termo
contador = 0

# Exibindo os 10 primeiros termos da PA usando a estrutura while
print("Os 10 primeiros termos da PA são:")
while contador < 10:
    print(termo, end=" ")
    termo += razao  # Atualiza o termo para o próximo
    contador += 1  # Conta os termos exibidos
