"""
8) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
"""

ganho_por_hora = float(input('Ganho por hora: '))
horas_trabalhadas = float(input('Horas trabalhadas no mês: '))
total_salario = ganho_por_hora * horas_trabalhadas
print('Salário Total no referido mês: R$', total_salario)