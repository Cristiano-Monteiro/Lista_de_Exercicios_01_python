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

# APENAS LATAS
if(cobertura % 18 == 0):
    quantidade_latas_apenas = cobertura / 18
else:
    quantidade_latas_apenas = int(cobertura / 18) + 1
preco_latas_apenas = quantidade_latas_apenas * 80

# APENAS GALÕES
if(cobertura % 3.6 == 0):
    quantidade_galoes_apenas = cobertura / 3.6
else:
    quantidade_galoes_apenas = int(cobertura /3.6) + 1
preco_galoes_apenas = quantidade_galoes_apenas * 25

# MISTURAR LATAS E GALÕES
quantidade_latas = int(cobertura / 18)
multiplo_parte_inteira = 18 * quantidade_latas
parte_fracionaria = cobertura - multiplo_parte_inteira
quantidade_galoes = int(parte_fracionaria / 3.6) + 1
preco_galoes = quantidade_galoes * 25
preco_latas = quantidade_latas * 80
preco_total = preco_latas + preco_galoes

print('Quantidade de latas APENAS:', quantidade_latas_apenas, end=' ------ ')
print('Preço Total das latas: R$', preco_latas_apenas)
print('Quantidade de galões APENAS:', quantidade_galoes_apenas, end=' ------ ')
print('Preço Total dos galões: R$', preco_galoes_apenas)
print('Misturar {} latas e {} galões ------ Preço Total: R$ {}'.format(quantidade_latas, quantidade_galoes, preco_total))