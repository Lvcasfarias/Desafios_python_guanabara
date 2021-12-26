print('-=-=-=-' * 10)
ptermo = int(input('Digite o primeiro Termo: '))
razao = int(input('Digite a razão: '))
termo = ptermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} --> ', end='')
        termo += razao
        cont +=1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais ? '))
print(f'Prog finalizada com {total} mostrados')
