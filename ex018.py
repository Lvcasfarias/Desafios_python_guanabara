#18: faça um programa que leia um angulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente

import math

desc = float(input('Digite um angulo: '))

print(f'Seno: {math.sin(math.radians(desc)):.2f}')
print(f'Coseno: {math.cos(math.radians(desc)):.2f}')
print(f'Tangente: {math.tan((math.radians(desc))):.2f}')

