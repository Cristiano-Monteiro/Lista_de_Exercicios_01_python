"""
17) Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que
a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam
R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
• comprar apenas latas de 18 litros;
• comprar apenas galões de 3,6 litros;
• misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga
e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
area = float(input('Tamanho da área(m²): '))
cobertura = area / 6
if(cobertura % 18 == 0):
    quantidade_latas = cobertura / 18
    quantidade_galoes = 0.0
    preco_galoes = 0.0
else:
    quantidade_latas = int(cobertura / 18)
    multiplo_parte_inteira = 18 * quantidade_latas
    parte_fracionaria = cobertura - multiplo_parte_inteira
    quantidade_galoes = int(parte_fracionaria / 3.6) + 1
    preco_galoes = quantidade_galoes * 25
preco_latas = quantidade_latas * 80
print('Quantidade de latas:', quantidade_latas, end=' ------ ')
print('Preço Total das latas: R$', preco_latas)
print('Quantidade de galões:', quantidade_galoes, end=' ------ ')
print('Preço Total dos galões: R$', preco_galoes)