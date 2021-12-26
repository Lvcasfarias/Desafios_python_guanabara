'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
cont = 0
while True:
    n = int(input('Diga um valor: '))
    pc = randint(0, 10)
    t = n + pc
    p = ' '
    while p not in 'PpIi':
        p = str(input('Par ou Impar?: ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador {pc} total de {t} ')
    if p == 'P':
        if t % 2 == 0:
            print('Você Venceu')
            cont += 1
        else:
            print('Você PERDEU!!!')
            break
    elif p == 'I':
        if t % 2 > 0:
            print('você Venceu')
            cont +=1
        else:
            print('Você PERDEU!!!')
            break
print(f'Você teve um total de {cont}, mas agora você perdeu')

