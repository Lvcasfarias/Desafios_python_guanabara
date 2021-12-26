#REFAÇA O DESAFIO 35 DOS TRIANGULOS ACRESCENANDO ALGUNS RECURSOS DE MOSTRAR QUE TIPO DE TRIANGULO SERÁ FORMADO
from time import sleep
print('-=-' * 10)
print('Analisador de Triangulos')
print('-=-'*10)
r1 = float(input('Digite o comprimento da Primeira reta: '))
r2 = float(input('Digite o comprimento da Segunda reta: '))
r3 = float(input('Digite o comprimento da Terceira reta: '))
#if r1 - r2 < r3 < r1 +r2:
#guanabara
if r1< r2 + 3 and r2 <r1 +3 and r3 < r1 +r2:
    print('Analisando...')
    sleep(2)
    if r1 == r2 == r3:
        print('É um triangulo EQUILÁTERO')
    if r1 != r2 !=r3 != r1:
        print('É um triangulo ESCALENO')
    else:
        print('é um triangulo ISOSCELES')
else:
    print('não é um triangulo')