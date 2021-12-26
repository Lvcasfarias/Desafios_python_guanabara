#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os
# . mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
from time import sleep
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
print('Fazendo a comparação...')
sleep(2)
if n1 > n2:
    print(f'O número {n1} é maior que o número {n2}')
elif n1 == n2:
    print(f'Os números {n1} e {n2} são iguais')
else:
    print(f'O número {n2} é maior que o número {n1}')
