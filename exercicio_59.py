# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso#
# Função principal do programa
while True:
    # Lê os dois valores iniciais
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))

    # Exibe o menu
    print("\nEscolha uma das opções:")
    print("[ 1 ] Somar")
    print("[ 2 ] Multiplicar")
    print("[ 3 ] Maior")
    print("[ 4 ] Novos números")
    print("[ 5 ] Sair do programa")

    # Lê a opção escolhida pelo usuário
    opcao = int(input("Digite a opção desejada: "))

    # Realiza a operação de acordo com a escolha
    if opcao == 1:
        soma = num1 + num2
        print(f"A soma entre {num1} e {num2} é: {soma}")
    elif opcao == 2:
        multiplicacao = num1 * num2
        print(f"A multiplicação entre {num1} e {num2} é: {multiplicacao}")
    elif opcao == 3:
        maior = max(num1, num2)
        print(f"O maior número entre {num1} e {num2} é: {maior}")
    elif opcao == 4:
        print("Você escolheu a opção de inserir novos números.\n")
        continue  # Volta ao início do laço e solicita novos números
    elif opcao == 5:
        print("Saindo do programa...")
        break  # Encerra o laço e o programa
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")

    print()  # Pula uma linha para facilitar a leitura entre as operações
