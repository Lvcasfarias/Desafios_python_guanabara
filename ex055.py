#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
somaidade = 0
for p in range(1, 5):
    print(f'----{p}----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

mediaidade = somaidade / 4
print(f'A media de idade do grupo é de {mediaidade} ano')