import ctypes
#ctypes.windll.user32.MessageBoxW(0,'O progama irá iniciar', 'Times',1)
times = ('América-MG','Athetico-PR','Atletico-MG','Bahia','Ceará SC','Chapecoense','Corinthias','Cuiabá','Flamengo',
         'Fluminense','Fortaleza','Gremio','Internacional','Juventude','Palmeiras','Bragantino','Santos','Sport Recife','São Paulo')
print('---'*20)
print(f'Lista de times do Brasileirão {times}')
print('---'*20)
print(f'Top 5 times do Brasileirao são {times[0:5]}')
print('---'*20)
print(f'Os 4 ultimos colocados são {times[15:21]}')
print('---'*20)
print(f'Times em ordem alfabetica{sorted(times)}')
print('---'*20)
print(f'O time Chapecoense está na posição {times.index("Chapecoense")+1}')
