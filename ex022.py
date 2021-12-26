#22: crie um programa que leia o nome completo de uma pessoa
#a: o nome com todas letras maiúsculas
#b: com todas letras minusculas
#c: quantas letras ao todo sem os espaços
#d: quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
maiusculo = nome.upper()
minusculo = nome.lower()
letras= len(nome ) - nome.count(' ')
primeiro = nome.split()[0]


print(f'O seu nome todo em maiúsculo é: {maiusculo} ')
print(f'O seu nome em minusculo é: {minusculo}')
print(f'A quantidade de caracteres do seu nome é: {letras}')
print(f'Seu primeiro nome é: {primeiro} E o Número {len(primeiro)}')

