#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a media atingida
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua seguda nota: '))
media = (n1 + n2) /2
if media <= 5.0:
    print(f'Sua media foi {media:.1f} você está reprovado, estude mais no proximo ano!')
elif media >= 5.0 and media <= 6.9:
    print(f'Sua media é de {media:.1f}, você está de recuperação')
else:
    print(f'Sua media é de {media:.1f}, você está aprovado, PARABÉNS!!')