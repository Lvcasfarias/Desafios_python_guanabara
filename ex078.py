lista = list()
for enum in range(5):
    lista.append(int(input(f'Digite um valor para a posição {enum}: ')))
    if enum == 0:
        maior = menor = lista[enum]
    if lista[enum] > maior:
        maior = lista[enum]
    if lista[enum] < menor:
        menor = lista[enum]
print(f'O maior número foi {maior} nas posições...')
for c, n in enumerate(lista):
    if lista[c] == maior:
     print(f'{c}...', end='')
print(f'O menor valor foi {menor} nas posições...')
for c, n in enumerate(lista):
    if lista[c] == menor:
        print(f'{c}...', end='')
lista.sort()
print(f'\nOs números digitados foram {lista}')
