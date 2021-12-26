#"Faça um Programa que leia um número inteiro menor que 1000
# e imprima a quantidade
# de centenas, dezenas e unidades do mesmo.

numero = int(input('Digite um número de 1 até 9999: '))
unidade = numero % 10
dezena = int((numero - unidade) / 10 % 10)
cent = int( (numero - dezena) / 100 % 10)
mil = int((numero-cent) / 1000 % 10)



print(f'O número {numero} tem {unidade} unidades\n'
      f' {dezena} dezenas\n'
      f' {cent} centenas\n'
      f'{mil} milhares')