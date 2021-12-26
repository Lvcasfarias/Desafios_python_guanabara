#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime
nasc = int(input('Qual a seu ano de nascimento: '))
sexo = int(input('Qual o seu Sexo ?\n'
                 '(1)... Homem\n'
                 '(2)... Mulher\n '))
ano = datetime.today().year
idade = ano - nasc
print(f'Quem naseu em {ano} tem/tera {idade} anos em 2021')

# Nesta parte dividimos os homens das mulheres

if sexo == 1:
    print('O Seu alistamento é Obrigatorio')
else:
    print('Por ser Mulher, o seu alistamnto não é Obrigatorio')


if idade == 18:
    print('Este ano você terá que se alistar')
elif idade > 18:
    print(f'Você deveria ter se alistado em {nasc + 18}')
else:
    print(f'Você ainda não tem 18 anos, faltam {(idade - 18) * -1}')