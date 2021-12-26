'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
pessoas = dict()
cadastros = list()
soma = media = 0
print('Bem vindo')
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo[F|M]: ')).upper()[0]
        if pessoas['sexo'] in 'FM':
            break
        print('Error! escolha entre F e M')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    cadastros.append(pessoas.copy())
    while True:
        go = str(input('Quer continuar? [S|N]')).upper()[0]
        if go in 'SN':
            break
        print('Error! Escolha entre S e N')
    if go in 'Nn':
        break
print('-='*30)
print(cadastros)
print(f'Foram cadastradas {len(cadastros)} pessoas')
media = soma / len(cadastros)
print(f'A media das idades é {int(media)}')
print(f'As mulheres cadastradas foram ', end='')
for p in cadastros:
    if pessoas['sexo'] == 'F':
        print(f'{p["nome"]}')
print('Lista das pessoas que estão acima da media')
for p in cadastros:
    if p['idade'] >= media:
        print('  ')
    for k,v in p.items():
        print(f'{k} = {v};')
print('Fim')