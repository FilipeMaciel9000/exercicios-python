#  Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
# Leitura do nome da pessoa
nome = input("Digite o nome da pessoa: ")

# Verifica se a palavra "SILVA" está presente no nome
if "SILVA" in nome.upper():
    print("O nome contém 'SILVA'.")
else:
    print("O nome não contém 'SILVA'.")
