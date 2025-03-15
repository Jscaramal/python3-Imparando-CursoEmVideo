#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
#No final, mostre:

#A- QUal é o total gasto na compra.
#B Quantos produtos custam mais de 1000 reais
#C qual é o nome do produto mais barato.
qtdMil = total = 0
nomePrdBarato = ""
precoPrdBarato = 0
print('-'*50)
print(f"{'LOJA SUPER BARATÃO':^50}")
print('-'*50)
while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    if total == 0:
        precoPrdBarato = preco
        nomePrdBarato = nome
    total += preco
    if preco > 1000:
        qtdMil += 1
    elif preco < precoPrdBarato:
        nomePrdBarato = nome
        precoPrdBarato = preco
    while True:
        continuar = str(input('Quer continuar? [S/N] : ')).strip().upper()[0]
        if continuar == 'N' or continuar == 'S':
            break
    if continuar == 'N':
        break
print('-'*50)
print('PROGRAMA ENCERRADO')
print('-'*50)
print(f'Total da compra: {total:.2f}')
print(f'Quantidade de produto que custa mais de R$1000 : {qtdMil:.2f}')
print(f'O produto mais barato é o {nomePrdBarato} que custa R${precoPrdBarato:.2f}')