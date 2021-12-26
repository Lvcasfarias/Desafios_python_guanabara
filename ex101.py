import datetime

def voto(nasci):
    ano = datetime.datetime.today().year
    idade = ano - nasci
    if idade < 16:
        print('Não vota!')
    elif idade >= 65:
        print('Voto Opicional!')
    else:
        print('VOTO Obrigatorio!')
    print(idade)


voto(int(input('Ano de nascimento: ')))