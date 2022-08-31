"""
9) Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura 
em graus Celsius. C = 5 * ((F-32) / 9).
"""

temperatura_fahrenheit = int(input('Digite uma temperatura em Fahrenheit: '))
conversao_celsius = 5 * ((temperatura_fahrenheit - 32) / 9)
print('Temperatura em Celsius:', conversao_celsius)