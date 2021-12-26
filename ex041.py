#a confederação nascional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua catergoria de acordo com a idade
from datetime import datetime
nasc = int(input('Qual o eu ano de nascimento ? '))
atual = datetime.today().year
idade = atual - nasc

if idade < 10:
    print('Você está na selação Mirim de natação')
elif idade < 15:
    print('VocÊ está na seleção infantil de natação')
elif idade < 20:
    print('Você está na seleção junior de natação')
elif idade < 26:
    print('VocÊ está na selação senior de natação')
else:
    print('VocÊ está na seleção master de natação')