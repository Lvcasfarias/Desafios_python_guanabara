print('-=-=-=-' * 10)
ptermo = int(input('Digite o primeiro Termo: '))
razao = int(input('Digite a razão: '))
termo = ptermo
cont = 1
while cont <= 10:
    print(f'{termo} --> ', end='')
    termo += razao
    cont +=1
print('fim')
