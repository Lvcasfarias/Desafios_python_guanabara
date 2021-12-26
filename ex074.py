from random import randint

n= (randint(1, 10), randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))
print(f'Os numeros aleatorios são {n}')
for num in n:
    print(f'{num} ', end='')
print(f'O maior Valor sorteado foi {max(n)} e o menor foi {min(n)}')