#Escrava um programa que lia a velocidade de um carro
#se ele ultrapassar 80km/h, mostre uma mnsagem dizendo que ele foi multado
#A multa vai csutar 7,00 por cada km acima do limite

velo = int(input('Qual a velocidade seu carro estava ? '))
km = 80 #Velocidade limite
multa = (velo - km) * 7 #Calculo da multa
if velo <= km:
    print(f'Você está dentro da velocidade limite de {km}km/h') #Dentro da velocidade
else: print(f'Você está acima da velocidade Limite de {km}km/h\n' #Multado
            f'E será multado em {multa}')