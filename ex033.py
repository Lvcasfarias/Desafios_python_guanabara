#
# 33: faça um programa que leia trÊs números e mostre
# ]qual é o maior e qual é o menor

# Igual o do professor
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c: int = int(input('Terceiro número: '))
menor = a  # Desta maneira o menor sempre será o A, mas quando ele for maior, será substituido
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando qual o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
