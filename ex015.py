#Escreva um programa que pergunt a quantidade de KM pecorridos por um carro
#E a quantidade de dias alugado e calcule o preço a pagar
#sabendo que o dia custa 60 e o km 0,15

dias = int(input('Quantos dias você ficou com o carro ?'))
km = float(input('Quantos Km vc rodou com o carro'))

calcdias = 60 * dias
calckm = 0.15 * km

vfinal = calckm + calcdias

print(f'O valor do Aluguel é de {vfinal}')