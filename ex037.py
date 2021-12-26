#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para
# octal e 3 para hexadecimal.
n1 = int(input('Digite um número: '))

n2 = int(input('Escolha a base de conversão\n'
      '[1]... binario\n'
      '[2]... octal\n'
      '[3]... hexadecimal '))
1 -

if n2 == 1:
    print(f'O numéro {n1} convertido para binario é {bin(n1)[2:]}')
elif n2 == 2:
    print(f'O número {n1} convertido para octal é {oct(n1)[2:]}')
elif n2 == 3:
    print(f'O número {n1} convertido para hexdecimal é {hex(n1)[2:]}')
else:
    print('Digite um dos números apresentados')