#  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#  Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#  A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
# Começo do mundo 2
# Solicitar os dados do comprador
valor_casa = float(input("Digite o valor da casa: R$ "))
salario_comprador = float(input("Digite o valor do salário do comprador: R$ "))
anos_pagamento = int(input("Digite em quantos anos o comprador vai pagar: "))

# Calcular o valor da prestação mensal
prestacao_mensal = valor_casa / (anos_pagamento * 12)

# Verificar se a prestação mensal excede 30% do salário
if prestacao_mensal <= 0.30 * salario_comprador:
    print("Empréstimo aprovado! Sua prestação mensal será de R$ {:.2f}".format(prestacao_mensal))
else:
    print("Empréstimo negado! A prestação mensal excede 30% do seu salário.")
