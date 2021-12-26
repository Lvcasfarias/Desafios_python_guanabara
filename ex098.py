from time import sleep
def contador(i,f,p):
     print(f'Contagem de {i} aé {f} de {p} em {p}')
     sleep(0.5)
     if p < 0:
          p *= -1
     if p == 0:
          p = 0
     if i < f:
          cont = i
          while cont <=f:
               print(f'{cont} ', end='')
               sleep(0.5)
               cont+= p
          print('FIM')
     else:
          cont = i
          while cont >= f:
               print(f'{cont} ', end='')
               sleep(0.5)
               cont -= p
          print('FIM')


contador(1,10, 1)
contador(10,0,2)
contador(i=int(input('inicio: ')), f=int(input('Fim: ')), p=int(input('Passo: ')))
