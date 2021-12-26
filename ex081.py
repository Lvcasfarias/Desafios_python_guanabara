lista = list()
while True:
    lista.append(int(input('Digite um número para a nossa lista: ')))
    continuar = str(input(' Você quer continuar ? Sim / Não ')).upper().strip()
    if continuar in 'Nn':
        break

lista.sort(reverse=True)
print(f'Está é sua lista: {lista}')
print(f'Você digitou {len(lista)} itens na nossa lista')
print(f'Esta é a sua lista ordenada com valor decrescente:{lista}')
if 5 in lista:
    print('O número 5 está Na lista')
else:
    print('O número 5 NÃO ESTÁ NA LISTA')
