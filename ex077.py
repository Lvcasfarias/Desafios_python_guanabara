lista =  ('Aprender', 'PROGRAMAR', 'lINGUAGEM','PYTHON','CURSO','GRATIS')
for vogal in lista:
    print(f'\nna palavra {vogal} temos:',end=' ')
    for letra in vogal:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')