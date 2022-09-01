"""
13) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso
ideal, utilizando as seguintes fórmulas:
• Para homens: (72.7*h) - 58
• Para mulheres: (62.1*h) - 44.7
"""
h = float(input('Digite uma altura(m): '))
peso_homens = (72.7 * h) - 58
peso_mulheres = (62.1 * h) - 44.7
print('Peso para Homens:', peso_homens)
print('Peso para Mulheres:', peso_mulheres)