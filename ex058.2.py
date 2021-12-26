from random import randint
comp = randint(0,100)
palpite = 0
acertou = False
#print(comp)
while not acertou:
    jogador = int(input('Lança um palpite: '))
    if comp == jogador:
        acertou = True
        palpite +=1
        print(f'você acertou com {palpite} palpites')
    else:
        palpite += 1
        if jogador > comp:
            print('Menos... tente novamente: ')
        else:
            print('Mais... tente novamente: ')