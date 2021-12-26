#parar = 0
#cont = 0
parar = cont = soma = 0 #Solução do Professor
parar = int (input ('Digite um numero, 999 para sair: '))
while  parar != 999:
   #parar = int (input ('Digite um numero, 999 para sair: '))
   soma += parar
   cont += 1
   parar = int(input('Digite um numero, 999 para sair: '))
#print(f'Você digitou {cont - 1} numeros e a soma entre eles foi {soma - 999}')
print(f'Você digitou {cont} numeros e a soma entre eles foi {soma}') #A solução do professor foi colocar a Flag depois da soma e do cont, para que não seja incluida no calculo




