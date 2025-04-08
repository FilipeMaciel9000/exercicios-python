#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
# Leitura da frase
frase = input("Digite uma frase: ").upper()  # Convertendo para maiúsculas para garantir a busca insensível a maiúsculas e minúsculas

# Contagem de quantas vezes a letra 'A' aparece
quantidade_a = frase.count("A")

# Encontrando a posição da primeira ocorrência de 'A'
primeira_posicao = frase.find("A") + 1  # A função find retorna a posição começando de 0, então somamos 1 para começar de 1

# Encontrando a posição da última ocorrência de 'A'
ultima_posicao = frase.rfind("A") + 1  # rfind retorna a última ocorrência, e somamos 1 da mesma forma

# Exibindo os resultados
print(f"A letra 'A' aparece {quantidade_a} vez(es) na frase.")
if quantidade_a > 0:
    print(f"A primeira ocorrência de 'A' está na posição {primeira_posicao}.")
    print(f"A última ocorrência de 'A' está na posição {ultima_posicao}.")
