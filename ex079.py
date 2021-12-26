#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
# serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = list()
while True:
    num = int(input('Digite um valor para nossa lista: '))
    if num not in lista:
        lista.append(num)
    else:
        print('número duplicado, vou ignorar...')
    cont = str(input('Quer continuar ? [S/N]')).strip().upper()
    if cont in 'Ss':
        print('Ok, vamos recomeçar')
    elif cont in 'Nn':
        break
    else:
        print('Error 404')
        break

lista.sort()
print(f'Está é sua lista {lista}')
