# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
# Leitura do nome da cidade
cidade = input("Digite o nome da cidade: ")

# Verifica se a cidade começa com "SANTO"
if cidade.strip().upper().startswith("SANTO"):
    print("A cidade começa com 'SANTO'.")
else:
    print("A cidade não começa com 'SANTO'.")
