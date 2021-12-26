# 20: leia  nome dos 4 anos e mostre a ordem sorteada
import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')

list = [n1,n2,n3,n4]

random.shuffle(list)

print(list)