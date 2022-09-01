"""
11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
• o produto do dobro do primeiro com metade do segundo.
• a soma do triplo do primeiro com o terceiro.
• o terceiro elevado ao cubo.
"""
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um número real: '))

A = (2 * n1) * (n2 / 2)
B = (3 * n1) + n3
C = n3 ** 3
print(A)
print(B)
print(C)