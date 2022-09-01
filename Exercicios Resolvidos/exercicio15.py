"""
15) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no
mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
• salário bruto.
• quanto pagou ao INSS.
• quanto pagou ao sindicato.
• o salário líquido.
• calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido
"""
ganho_hora = float(input('Ganho por hora: '))
horas_trabalhadas = int(input('Horas trabalhadas no mês: '))
salario_bruto = ganho_hora * horas_trabalhadas
imposto_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)
print('Salário Bruto: R$', salario_bruto)
print('Gasto com INSS: R$', inss)
print('Gasto com Sindicato: R$', sindicato)
print('Salário Líquido: R$', salario_liquido)