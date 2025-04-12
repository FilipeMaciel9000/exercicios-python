# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# Leitura do número N
N = int(input("Digite um número inteiro N para mostrar os primeiros N elementos da sequência de Fibonacci: "))

# Inicializando os dois primeiros termos da sequência
a, b = 0, 1

# Exibindo os N primeiros termos da sequência de Fibonacci
print(f"Os {N} primeiros termos da sequência de Fibonacci são:")

# Caso N seja 1, mostramos apenas o primeiro termo (0)
if N == 1:
    print(a)
else:
    for i in range(N):
        print(a, end=" ")
        a, b = b, a + b  # Atualiza os valores de a e b para o próximo termo
