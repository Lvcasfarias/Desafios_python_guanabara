#26: um programa que leia uma frase
#a: quantas vezes aparece a letra "a"
#b: em que posição ela aparece a primeira vez
#c: em que posição ela aparece na ultima vez

frase = str (input('Digite uma frase qualquer: ')).upper().strip()
print(f'A letra A aparece {frase.count("A")}')
print(f'A letra A aparece na posição {frase.find("A")+1}\n'
      f'A ultima Letra A aparece na posição {frase.rfind("A")+1}')
