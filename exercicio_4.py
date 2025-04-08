# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
# Queimei largada e usei funções, mas o código ainda está bem intuitivo.

def disseca_variavel(var):
    # Exibe o valor da variável e seu tipo
    print(f'Valor da variável: {var}')
    print(f'Tipo da variável: {type(var)}')

    # Verifica se a variável é um número (int, float ou complex)
    if isinstance(var, (int, float, complex)):
        print(f'É um número? {True}')  # Informa que é um número
        print(f'Valor absoluto (se for número): {abs(var)}')  # Exibe o valor absoluto do número
        if isinstance(var, int):  # Se for inteiro, mostra representações em diferentes bases
            print(f'Valor binário (se inteiro): {bin(var)}')  # Exibe o valor binário
            print(f'Valor octal (se inteiro): {oct(var)}')    # Exibe o valor octal
            print(f'Valor hexadecimal (se inteiro): {hex(var)}')  # Exibe o valor hexadecimal

    # Verifica se a variável é uma string
    elif isinstance(var, str):
        print(f'É uma string? {True}')  # Informa que é uma string
        print(f'Tamanho da string: {len(var)}')  # Exibe o tamanho da string
        print(f'Primeira letra (se string): {var[0] if len(var) > 0 else "Vazia"}')  # Exibe a primeira letra
        print(f'Última letra (se string): {var[-1] if len(var) > 0 else "Vazia"}')  # Exibe a última letra
        print(f'String maiúscula: {var.upper()}')  # Exibe a string em maiúsculas
        print(f'String minúscula: {var.lower()}')  # Exibe a string em minúsculas
        print(f'String invertida: {var[::-1]}')  # Exibe a string invertida

    # Verifica se a variável é uma lista
    elif isinstance(var, list):
        print(f'É uma lista? {True}')  # Informa que é uma lista
        print(f'Tamanho da lista: {len(var)}')  # Exibe o tamanho da lista
        print(f'Primeiro elemento (se lista): {var[0] if len(var) > 0 else "Lista vazia"}')  # Exibe o primeiro elemento
        print(f'Último elemento (se lista): {var[-1] if len(var) > 0 else "Lista vazia"}')  # Exibe o último elemento
        print(f'Lista ordenada: {sorted(var)}')  # Exibe a lista ordenada

    # Verifica se a variável é um dicionário
    elif isinstance(var, dict):
        print(f'É um dicionário? {True}')  # Informa que é um dicionário
        print(f'Número de chaves: {len(var)}')  # Exibe o número de chaves do dicionário
        print(f'Chaves do dicionário: {list(var.keys())}')  # Exibe as chaves do dicionário
        print(f'Valores do dicionário: {list(var.values())}')  # Exibe os valores do dicionário

    # Verifica se a variável é um valor booleano
    elif isinstance(var, bool):
        print(f'É um valor booleano? {True}')  # Informa que é um booleano
        print(f'Valor invertido (NOT): {not var}')  # Exibe o valor invertido (operação NOT)

    # Exibe a possibilidade de conversão para outros tipos
    print(f'Pode ser convertido para booleano? {bool(var)}')  # Verifica se pode ser convertido para booleano
    print(f'Pode ser convertido para inteiro? {isinstance(var, (int))}')  # Verifica se pode ser convertido para inteiro
    print(f'Pode ser convertido para string? {isinstance(var, (str))}')  # Verifica se pode ser convertido para string
    print(f'Pode ser convertido para lista? {isinstance(var, (list))}')  # Verifica se pode ser convertido para lista

# Solicita ao usuário a entrada de uma variável para dissecação
variavel = input("Digite algo: ")

# Verifica se a entrada é um número (somente dígitos)
if variavel.isdigit():
    variavel = int(variavel)  # Converte para inteiro se for um número

# Chama a função para dissecação da variável
disseca_variavel(variavel)
