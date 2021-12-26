sexo = str(input('Informe seu sexo [M|F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('dados invalidos  : ')).upper().strip()[0]
print(f'Sexo {sexo}')