import time
from random import randint
from operator import itemgetter
from time import sleep
jogos = {'Jogador 1':randint(1,6),
             'jogador 2':randint(1,6),
             'jogador 3':randint(1,6),
             'jogador 4':randint(1,6)}
ranking = list()
print('-=-=-=-=-=-Valores sorteados-=-=-=-=-=-=')
for k, v in jogos.items():
    print(f'{k} tirou {v} nos dados')
    time.sleep(1)
print('-=--='*10)
print('>>>>RANKING DE JOGADORES<<<<')
ranking = sorted(jogos.items(), key=itemgetter(1),reverse=True)
for i, v in enumerate(ranking):
    time.sleep(1)
    print(f'{i + 1} lugar: {v[0]} com {v[1]}.')