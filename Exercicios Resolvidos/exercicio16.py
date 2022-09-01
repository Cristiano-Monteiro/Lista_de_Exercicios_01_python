"""
16) Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que
a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas
de tinta a serem compradas e o preço total.
"""
area = float(input('Tamanho da área(m²): '))
cobertura = area / 3
if(cobertura % 18 == 0):
    quantidade_latas = cobertura / 18
else:
    quantidade_latas = int(cobertura / 18) + 1
preco = quantidade_latas * 80
print('Quantidade de latas:', quantidade_latas)
print('Preço Total: R$', preco)

"""
OBS: Explicação sobre 'quantidade_latas = int(cobertura / 18) + 1':
    Se a cobertura dividido por 18 resultar em um número real(6.753, por exemplo), então pegamos a parte 
    inteira dele(6) e o restante(0.753), por não ser possível comprar '0.7 latas', arredondamos para 1,
    resultando em 7 latas, nesse exemplo.
"""