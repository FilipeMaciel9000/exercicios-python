#  Escreva um programa que leia a velocidade de um carro.
#  Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.
# Leitura da velocidade do carro
velocidade = float(input("Digite a velocidade do carro (em Km/h): "))

# Verificando se a velocidade ultrapassa o limite de 80 Km/h
if velocidade > 80:
    # Calculando o valor da multa
    excesso = velocidade - 80
    multa = excesso * 7  # R$7,00 por Km acima do limite
    print(f"Você foi multado! O valor da multa é R${multa:.2f}.")
else:
    print("A velocidade está dentro do limite. Você não foi multado.")
