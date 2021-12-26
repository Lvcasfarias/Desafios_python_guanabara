#24: crie um programq ue leia o nome de uma
# cidade se ela começa ou não com a palavra santo

cidade = str(input('Digite o nome de uma cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')
