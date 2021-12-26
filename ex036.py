#Exercício Python 36: Escreva um programa para aprovar o
# empréstimo bancário para a compra de uma casa. Pergunte
# o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar. A prestação mensal
# não pode exceder 30% do salário ou então o empréstimo será negado.

salario = float(input('Qual é o seu salario ? '))
casa = float(input('Qual o valor da casa que vocÊ quer comprar ? '))
tempo = float(input('Em quantos anos você pretende comprar a casa ?'))
prestacao = casa / (tempo * 12)
minimo = salario * 30 / 100
print(f'Para comprar uma casa de {casa} o valor da prestação será de {prestacao}')
if salario <= minimo:
    print('Emprestimo concedido! ')
else:
    print('Emprestimo Negado!')
