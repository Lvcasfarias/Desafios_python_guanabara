'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''

alunos = {}
while True:
    alunos['nome']= str(input('NOME: '))
    alunos['media']= float(input(f'Media de {alunos["nome"]}: '))
    if alunos['media'] <= 3:
        alunos['Situação'] = 'Reprovado'
    elif alunos['media'] <= 6:
        alunos['Situação'] = 'Recuperação'
    elif alunos['media'] > 6:
        alunos['Situação'] = 'Aprovado'
    cont = str(input('Quer continuar?'))
    if cont in 'Nn':
        break
print(alunos['Aprovado'])
print(alunos['Reprovado'])