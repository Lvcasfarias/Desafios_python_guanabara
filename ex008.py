#8: escreva um programa que leia um valor em metros e
# exiba convertido em centimetros e milimetros
metros= float(input('Digite uma Distancia em metros: '))
dm = metros * 10
cm = metros * 100
mm = metros * 1000
dam = metros / 10
hm = metros / 100
km = metros / 1000

print(f'A distancia {metros:} convertida para:\n'
      f'decimetros é igual a: {dm:}\n'
      f'Centimetros: {cm:}\n'
      f'Milimetros: {mm}\n'
      f'Decametro: {dam}\n'
      f'hectometro: {hm}\n'
      f'Kilometros: {km}')
