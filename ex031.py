#Faça um programa que pergunte a distancia de uma viagem em KM, calcule
# o preço da passagem do onibus
#Cobrando 0,50 por km de viagem até 200km e 0,45 para viagens mais longas

'''viagem = int(input('Qual a distancia da sua viagem em KM?: '))

if viagem <= 200:
    print(f'O preço da sua passagem é de R${viagem * 0.50}')
else:
    print(f'O preço da sua passagem é de R${viagem * 0.45}')'''

#igual o do guanabara

distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}km')
if distancia <= 200:
    preco = distancia * 0.50
    print(f'O valor da sua passagem é de R${preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'O valor da sua passagem será de R${preco:.2f}')