import time
from datetime import datetime

funcionario = dict()
funcionario['Nome:'] = str(input('Nome: '))
funcionario['Nasci:'] = int(input('Ano de nascimento: '))
funcionario['Carteira:'] = int(input('Número da Carteira 0 = não tem: '))
if funcionario['Carteira:'] != 0:
    funcionario['Contratação:'] = int(input('Ano de contratação: '))
    funcionario['salario:'] = float(input('Qual seu salario: '))
    funcionario['aposentadoria:'] = funcionario['Nasci:'] + ((funcionario['Contratação:'] + 35 ) - datetime.now().year)

for k, v in funcionario.items():
    print(f'{k}  {v}')
