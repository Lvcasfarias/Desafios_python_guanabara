numeros = ('zero','um', 'dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze',
           'treze','catorze', 'quinze', 'dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num =int(input('Digite um número entre 0 e doze '))
    if num >= 21 or num <= 0:
        print('Numero fora do nosso range, tente novamente')
    else:
        print(numeros[num])
    continuar = str(input('VOcÊ quer continuar ? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break

print('Volte sempre!')
