#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
altura = float(input('Qual a sua altura ?(m) '))
peso = float(input('Qual o seu peso ?(Kg) '))
imc = peso / (altura ** 2 )
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}, você está abaixo do peso')
elif 25 > imc > 18.5:
    print(f'Seu IMC é de {imc:.1f}, você está no peso ideal')
elif 30 > imc > 25:
    print(f'Seu ICM é de {imc:.1f}, você está com sobrepeso')
elif 40 > imc > 30:
    print(f'Seu ICM é de {imc:.1f}, você está com obesidade')

else:
    print('você está com obesidade mórbida')