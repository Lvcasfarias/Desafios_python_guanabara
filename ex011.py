#faça um programa que leia a largura e a altura de uma parede
# , calcule a sua área e calcule a quantidade de tinta
# necessaria para pintar, sabendo que cada litro pinta 2m2.

altura = float ( input('Qual a altura da sua parede ?'))
largura = float(input('Qual a largura da sua parede ?'))
area = altura * largura
tinta = area / 2

print(f'A área da sua parede é de {area}m quadrados e quantidade de tinta\n '
      f'necessaria para pintar a sua parede será de {tinta:.2f}L')
