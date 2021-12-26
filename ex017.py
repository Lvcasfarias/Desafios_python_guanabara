#Faça um programa que leia o comprimento do cateto opostp
#Cateto adjacente e calcule sua hipotenusa
import math
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente'))

#hipo = (oposto ** 2) + (adjacente ** 2)
#final = sqrt(hipo)
#correção
final = math.hypot(oposto, adjacente)

print(f'O cateto oposto deste triangulo retangulo é: {oposto}\n'
      f'O cateto adjacente dest triangulo retangulo é: {adjacente}\n'
      f'A hipotenusa deste triangulo retangulo é: {final:.2f}\n')