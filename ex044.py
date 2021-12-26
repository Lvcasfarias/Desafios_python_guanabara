#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
produto = float(input('Qual o valor do seu produto ? '))
pag = int(input('Qual será a porta de pagamento do seu produto ?\n'
            '[1]... À vista com 10% de desconto\n'
            '[2]... À vista no cartão com 5% de desconto\n'
            '[3]... 2x no cartão sem juros\n'
            '[4]... 4x ou mais no cartão com acrescimo de 20%'))
if pag == 1:
    total = produto - (produto * 10 / 100)
elif pag == 2:
    total = produto - (produto * 5 / 100)
elif pag == 3:
    total = produto / 2
elif pag == 4:
    total = produto + (produto * 20 / 100)
else:
    print('ESCOLLHA UMA OPÇÃO VALIDA!')
print(f'A sua compra de {produto} ficará por {total}')
