# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time

# Contagem regressiva de 10 até 0
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)  # Pausa de 1 segundo

# Após a contagem, exibe a mensagem de estouro dos fogos
print("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *FOGOS DE ARTIFÍCIO!!!*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)")
