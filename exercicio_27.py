# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Leitura do nome completo
nome_completo = input("Digite o seu nome completo: ")

# Dividir o nome em partes (usando o espaço como separador)
nome_parts = nome_completo.split()

# Exibir o primeiro e o último nome
primeiro_nome = nome_parts[0]
ultimo_nome = nome_parts[-1]

# Exibindo os resultados
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
