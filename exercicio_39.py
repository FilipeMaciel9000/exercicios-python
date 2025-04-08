# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime

# Solicitar o ano de nascimento do jovem
ano_nascimento = int(input("Digite o seu ano de nascimento: "))

# Obter o ano atual
ano_atual = datetime.now().year

# Calcular a idade do jovem
idade = ano_atual - ano_nascimento

# Determinar a situação do alistamento
idade_alistamento = 18
diferenca = abs(idade - idade_alistamento)

if idade < idade_alistamento:
    print(f"Ainda falta {diferenca} anos para o alistamento.")
elif idade == idade_alistamento:
    print("Agora é a hora exata de se alistar!")
else:
    print(f"Já passou {diferenca} anos do prazo para o alistamento.")
