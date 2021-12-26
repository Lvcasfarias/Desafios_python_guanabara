# faça um programa que leia um nome completo de uma pessoa
#e mostre em seguida o priemeiro e ultimo nome separadamente

n = str(input('Qual o seu nome completo ?: ')).strip()
nome = n.split()

print(f'Seu primeiro nome é {nome[0]}\n'
      f'Seu ultimo nome é {nome[len(nome)-1]}')