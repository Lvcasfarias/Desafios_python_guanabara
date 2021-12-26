soma = quant = media = maior = menor = 0
continuar = 'S'
while continuar in 'Ss':
    n1 = int(input('Digite um número ?'))
    soma += n1
    quant +=1
    if quant == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    continuar = str(input('Quer continuar ? [S|N] ')).upper().strip()[0]
média = soma / quant
print(f'Você digitou {quant} e a media foi {média}')
print(f'o maior foi {maior} e o menor foi {menor}')