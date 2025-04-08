#  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import datetime

# Solicitar o ano de nascimento do atleta
ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))

# Obter o ano atual
ano_atual = datetime.now().year

# Calcular a idade do atleta
idade = ano_atual - ano_nascimento

# Determinar a categoria de acordo com a idade
if idade <= 9:
    categoria = "MIRIM"
elif idade <= 14:
    categoria = "INFANTIL"
elif idade <= 19:
    categoria = "JÚNIOR"
elif idade <= 25:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"

# Exibir a categoria do atleta
print(f"O atleta tem {idade} anos e sua categoria é: {categoria}")
