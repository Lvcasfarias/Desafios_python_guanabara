'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
 cadastre-os em uma lista única que mantenha
 separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
num = [[],[]]
#par = []
#impar = []
valores = 0
'''for numeros in range(7):
    valores = (int(input('Digite um número: ')))
    num.append(valores)
    if valores % 2 == 0:
        par.append(valores)
    else:
        impar.append(valores)''' #MINHA RESPOSTA
#RESPOSTA DO GUANABARA
for c in range(1,8):
    valores = int((input(f'Digite um {c} valor: ')))
    if valores % 2 == 0:
        num[0].append(valores)
    else:
        num[1].append(valores)
#print(num)
#print(impar)
#print(par)
print(f'Está é sua lista principal {num}\n está é sua lista de pares {num[0]} \n está é sua lista de impares {num[1]}')