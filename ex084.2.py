#Resposta do professor para o exercicio 84
#Ele cadastra cada pessoa em uma lista "diferente", enquanto eu fiz tudo com apenas uma lista
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(int(input('Digite seu peso: ')))
    if len(princ) == 0:
        mai = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp)
    temp.clear()
    resp = str(input('Quer continuar ? [S/N]'))
    if resp in 'Nn':
        break
print(f'Os dados foram {princ}')
print(f'O mais pesado foi {maior:.2f}kg')
for p in princ:
    if p[1] ==maior:
        print(f'{p[0]}')
print(f'O menor peso foi {menor:.2f}')
print(f'Foram cadastra {len(princ)} pessoas')