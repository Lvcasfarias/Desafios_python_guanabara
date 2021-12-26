import time
from random import randint
from operator import itemgetter
from time import sleep
maior = 0
jogadores = dict()
ranking = dict()
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=> JOGO DOS DADOS <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
for j in range(1, 5):
    jogadores['dados']= randint(1, 6)
    print(f'O jogador {j} tirou: {jogadores["dados"]}')
    #time.sleep(1)
print('-=-=-=-=-=-=-='*10)
print('RANKING DOS JOGADORES')
ranking = sorted(jogadores(1))
print(ranking)

