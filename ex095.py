from operator import itemgetter
jogador = dict()
time = list()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas Partidas {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range (0, tot):
        partidas.append(int(input(f'Qauntos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S|N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>4}',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
