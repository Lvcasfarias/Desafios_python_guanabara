from operator import itemgetter
jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
for c in range(jogador['partidas']):
    gols.append( int(input(f'Quantos gols na partida {c + 1}: ')))
    total = sum(gols)
    jogador['gols'] = gols
    jogador['Total'] = total
print(jogador)
print('-=-=' *10)
for k, v in jogador.items():
    print(f'O campo {k} tem valor: {v}')
print('-=-=' *10)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i + 1}, fez {v}')
