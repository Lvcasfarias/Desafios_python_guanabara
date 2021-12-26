def maior (*num):
    cont = maior = 0
    for  n in num:
        print(n, end='')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
            cont +=1
    print(f' {cont} ')
    print(f'{maior}', end=' ')
'''while True:
   maior = int(input('Número: '))
    continuar = str(input('Quer continuar ? [s|n]'))
    if continuar in 'Nn':
        break
'''
maior(5, 15, 26, 49, 215, 3612)