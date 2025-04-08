# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# Solicita ao usuário o número para mostrar a tabuada
n = int(input('Digite um número: '))

# Exibe a mensagem inicial com o número escolhido
print(f'Tabuada de {n}:')

# Laço for para calcular e exibir a tabuada de 1 a 10
for i in range(1, 11):
    print(f'{n} * {i} = {i * n}')
