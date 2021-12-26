#JOKENPÔ
import random
lista = ['PEDRA', 'PAPEL','TESOURA']
escolha = str(input('Ola, vamos jogar JOKENPÔ, escolha entre pedra, papel e tesoura: ')).upper()
pc = random.choice(lista)
print(pc)

if escolha == pc:
    print(f'O pc esolheu {pc}, por isso deu empate')
elif escolha == 'PEDRA' and pc == 'PAPEL':
    print('VocÊ perdeu!')
elif escolha == 'PEDRA' and pc == 'TESOURA':
    print('VocÊ ganhou!')
elif escolha == 'TESOURA' and pc == 'PAPEL':
    print('Você ganhou!')
elif escolha == 'PAPEL' and pc == 'PEDRA':
    print('VocÊ perdeu!')
else:
    print('VOcÊ perdeu')

