print('-=-=-=-=-=-=-=-=-=- BOLETIM -=-=-=-=-=-=-=-=-=-')
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota = float(input('Nota: '))
    nota2 = float(input('Nota 2: '))
    media = (nota + nota2) / 2
    resp = str(input('Quer continuar? [S|N]'))
    ficha.append([nome, [nota, nota2], media])
    if resp in 'Nn':
        break
print(f'{"no.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO.....')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc] [0]} são {ficha[opc] [1]}')
print('=== VOLTE SEMPRE ===')  

   
