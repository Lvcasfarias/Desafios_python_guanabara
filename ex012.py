#Faça um programa qu leia o preo de um produto
#e calcule o desconto de 5%

preco = float(input('Qual o preço do seu produto?'))
desconto = preco * 5/100
final = preco - desconto

print(f'O valor do seu desconto será de {desconto}. O valor final com desconto é de {final}')