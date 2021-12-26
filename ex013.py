#13: faça um algoritimo que leia o salario de um fucionario e
# mostre seu novo salario com 15% de aumento

salario = float(input('Qual o seu salario ?'))
aumento = 15/100 * salario
final = aumento + salario

print(f'Seu salario é de: {salario}\n'
      f'O aumento de 15% é equivalente á {aumento:.2f} R$\n'
      f'Seu salario final com o Aumento de 15% é de {final:.2f}R$')