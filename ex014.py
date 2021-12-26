#Conversor de temperatura C para FH
celsius= float(input('Qual a temperatura em C?'))
fah = celsius *9/5 +32
kelvin= celsius+273,15
print(f'A temperatura {celsius}C é equivalent a {fah} Fahrenheit e '
      f'{kelvin} Graus Kelvin')