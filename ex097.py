def escreva(l):
    tam = len(l) +4
    print('~'* tam)
    print(f'  {l}')
    print('~' * tam)


while True:
    escreva(str(input('frase: ')))