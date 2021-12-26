print("-=-" * 10)
print('Bem vindo!')
print("-=-" * 10)
pessoas = list()
pesado = leve = 0
while True:
    nome = str(input('Digite seu nome: '))
    peso = float(input('Digite seu peso: '))
    continuar = str(input('Quer continuar ? [S/N]'))
    pessoas.append(nome)
    pessoas.append(peso)
    for p in pessoas:
        if peso > pesado:
            pesado = peso
            pessoapesada =nome
        else:
            leve = peso
            pessoaleve = nome
    if continuar in 'Nn':
        break
print(pessoas)
print(f'A pessoa mais pesada é {pessoapesada} pesando {pesado:.2f}Kg')
print(f'A pessoa mais leve é {pessoaleve} pesando {leve:.2f}Kg')