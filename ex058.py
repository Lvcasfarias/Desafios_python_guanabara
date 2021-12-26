from random import randint
n1 = randint(0, 100)
#print(n1)
n2 = int(input('Tente adivinhar qual número o computador pensou: '))
cont = 0
while n1 != n2:
    if n2 > n1:
        n2 = int(input('Menos, tente novamente: '))
        cont += 1
    else:
        n2 = int(input('Mais, tente novamente: '))
        cont += 1
print(f'Você acertou com {cont} tentativas')
