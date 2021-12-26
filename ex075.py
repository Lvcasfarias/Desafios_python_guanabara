cont = 0

n1 = (int(input('Digite um número: ')),
      int(input('Digite um número: ')),
      int(input('Digite um número: ')),
      int(input('Digite um número: ')))

print(f'VocÊ digitou os valores {n1}')
print(f'O número 9 foi digitado {n1.count(9)}')
if 3 in n1:
      print(f'O número 3 apareceu na posição {n1.index(3) + 1}')
else:
      print('O número 3 não apareceu')
print('Os valores pares digitados foram ', end=' ')
for n in n1:
      if n % 2 == 0:
            print(n, end=', ')