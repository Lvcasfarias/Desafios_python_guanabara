print('______' * 10)
print('Lista de Compras')
print('______' * 10)
mil = total = menor =  cont = 0
while True:
    produto = str(input('Qual o nome do Produto ? '))
    preço = float(input('Qual o valor do Produto ? '))
    cont +=1
    resp = ' '
    total += preço
    if preço >= 1000:
        mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    while resp not in 'SsNn':
        resp = str(input('Cadastrar novo produto[S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total foi de R${total:.2f}\n'
      f' {cont} Produtos com o valor acima de R$ 1000\n'
      f'O menor valor foi {menor} do produto {barato} ')