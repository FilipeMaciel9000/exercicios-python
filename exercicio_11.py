# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule sua área e a quantidade de tinta necessária para pintá-la.
# Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da parede (m): '))
altura = float(input('Digite a altura da parede (m): '))

# Cálculo da área e da quantidade de tinta necessária
area = largura * altura
tinta = area / 2

# Exibição dos resultados formatados
print(f'Para uma parede de {largura:.2f}m de largura e {altura:.2f}m de altura,')
print(f'temos uma área de {area:.2f}m².')
print(f'Você precisará de {tinta:.2f}L de tinta para pintá-la.')
