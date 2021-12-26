#19:um professor quer sortear um dos seus quatro alunos para apagar o
#quadro, faça um program que sortei aleatoreamente
import random
aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Teceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')

aleatorio = [aluno1,aluno2,aluno3,aluno4]
esco=random.choice(aleatorio)

print(f'O aluno escolhido foi {esco}')