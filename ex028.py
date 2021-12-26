#escreva um programa que faça o computador "Pensar" em um número de 0 a 5
#e peça para o usuário tentar descobrir qual é o número
#o programa devera escrever na tela se o usuário venceu ou perdeu
import random
from time import sleep

print('-=-' *10 )
print('Vou pensar em um número de 0 a 5, tente adivinhar ') #Computador fala#
print('-=-'*10)
num = int(input('Em qual número eu pensei: '))#Jogador tenta adivinhar
print('Processando...')
sleep(2)
valor = random.randint(0, 5)


if num == valor:
    print('Você acertou!')# Jogador venceu
else:
    print('Você errou\n'
          f'O número era: {valor}')# Jogador perdeu


