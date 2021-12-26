'''34: escreva um programa que pergunte o salario e calcule o valor do aumento
para salario superiores a 1,250 calcule um aumento de 10%'''

sal = float(input('Qual o seu salario ? R$'))

if sal >= 1250:
    aumento = sal * 1.1
    print(f'Seu salario de R${sal} agora será de R${aumento:.2f}')
else:
    aumento = sal * 1.15
    print(f'Seu salario de R${sal} agora será de R${aumento:.2f}')