#crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

maior = 0
menor = 0
atual = date.today().year
for c in range(0, 7):
    ano = int(input(f'Digite o ano de nascimento: '))
    ano = atual - ano
    if ano >= 21:
        maior += 1
    else:
        menor += 1
print(f'Dos anos qe digitou temos. \nMaiores de idade: {maior} \n Menores de idade: {menor}')