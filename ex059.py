n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('''
    [1] somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} e {n2} foi de {soma}')
    elif opcao == 2:
        multi = n1 * n2
        print(f'O resultado da multiplicação é {multi}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O {n1} é maior que o {n2}')
        elif n1 < n2:
            print(f'O {n1} é menor que o {n2}')
        else:
            print('Os números são iguais')
    elif opcao == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao == 5:
        print('Estamos fechando o programa!')
    else:
        print('Opção invalida!')
    print('=-=-=-=-' * 10)
print('Fim do programa, volte sempre!')
