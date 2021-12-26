print('~~~~' * 20)
print('FORMULARIO DE CADASTRO')
print('~~~~' * 20)
mais = menos = homem = total = 0
while True:
    #nome = str(input('Qual o seu nome ? ')).strip()
    idade = int(input('Qual a sua idade ? '))
    genero = ' '
    while genero not in 'MF':
        genero = str(input('Com qual Genero você se identifica[M/F] ?')).strip().upper()[0]
    cadastro = ' '

    if idade > 18:
        mais += 1
    if genero in 'Ff' and idade < 20:
        menos += 1
    if genero in 'Mm':
        homem += 1
    while cadastro not in 'SN':
        cadastro = str(input('Quer Continuar com os Cadastros [S/N]')).strip().upper()[0]
    if cadastro == 'N':
        break
print(f'Os cadastros terminaram...\n'
      f'Do total de pessoas cadastradas {mais} são maiores de 18 anos\n'
      f'{homem} são homens\n'
      f'{menos} são mulheres abaixo de 20 anos')
print('Acabou')
