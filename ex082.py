lista = list()
impar = list()
par = list()
while True:
    valor = int(input('Digite um valor para nossa lista: '))
    lista.append(valor)
    keep = str(input('Você quer continuar ? [S/N]'))
    if keep in 'Nn':
        break
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'Está é sua lista {lista}')
print(f'Está é sua lista de números pares {par}')
print(f'Está é sua lista de números impares {impar}')
print('fim')