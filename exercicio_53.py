# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
# Leitura da frase
frase = input("Digite uma frase: ").strip()

# Remover espaços e colocar tudo em minúsculas para comparar de forma correta
frase_sem_espacos = frase.replace(" ", "").lower()

# Verificar se a frase é igual ao seu reverso
if frase_sem_espacos == frase_sem_espacos[::-1]:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")
