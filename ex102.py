def fatorial(show=False):
    """
    Calcula o Fatorial de um número
    :param n: O número que será calculado
    :param show: (Opicional) Mostra o não a conta
    :return: O valor d fatorial de um número N
    """
    n = int(input('Digite o valor de N: '))
    mostrar = str(input('Ver calculo? [S|N]')).strip()
    if mostrar in 'Ss':
        show = True
    elif mostrar in 'Nn':
        show = False
    else:
        print('Parametro errado')
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    print(f)
    return f



fatorial()