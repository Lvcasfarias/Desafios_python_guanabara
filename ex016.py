#Crie um programa que leia um número real qualquer pelo teclado e mostre a sua parte inteira
from math import trunc
ent = (float(input('Digite um número real: ')))


#print(f'O numero {math.floor(ent)}')

#Resolução
print(f'O valor digitado foi {ent} e sua porção inteira é {trunc(ent)}')