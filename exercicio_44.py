# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
# Solicitar o preço do produto
preco = float(input("Digite o preço do produto: R$ "))

# Exibir as opções de pagamento
print("""
Escolha a forma de pagamento:
1 - À vista no dinheiro/cheque (10% de desconto)
2 - À vista no cartão (5% de desconto)
3 - Em até 2x no cartão (sem desconto)
4 - 3x ou mais no cartão (20% de juros)
""")
opcao = int(input("Digite a opção escolhida (1/2/3/4): "))

# Calcular o valor a ser pago de acordo com a forma de pagamento
if opcao == 1:
    # À vista no dinheiro/cheque (10% de desconto)
    valor_final = preco * 0.90
    print(f"Pagamento à vista no dinheiro/cheque. Valor com 10% de desconto: R$ {valor_final:.2f}")
elif opcao == 2:
    # À vista no cartão (5% de desconto)
    valor_final = preco * 0.95
    print(f"Pagamento à vista no cartão. Valor com 5% de desconto: R$ {valor_final:.2f}")
elif opcao == 3:
    # Em até 2x no cartão (sem desconto)
    parcelas = 2
    valor_parcela = preco / parcelas
    print(f"Pagamento em até 2x no cartão. Valor por parcela: R$ {valor_parcela:.2f} (sem juros)")
elif opcao == 4:
    # 3x ou mais no cartão (20% de juros)
    parcelas = int(input("Digite em quantas vezes você quer parcelar (3 ou mais): "))
    valor_final = preco * 1.20
    valor_parcela = valor_final / parcelas
    print(f"Pagamento em {parcelas}x no cartão. Valor com 20% de juros: R$ {valor_final:.2f}")
    print(f"Valor por parcela: R$ {valor_parcela:.2f}")
else:
    print("Opção inválida. Tente novamente.")
