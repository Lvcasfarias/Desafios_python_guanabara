#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dolares ela pode comprar 3.15

saldo = float(input('Quanto dinherio você tem na carteira? R$ '))
dolar = 3.27
dol = saldo / dolar

print(f'Com {saldo} você consegue comprar {dol:.2f} dolare(s)')