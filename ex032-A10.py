#faça um progrma que leia um ano qualque e mostre se ele é bissexto
from datetime import date

ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))
ano = date.today().year if ano == 0 else ano

print(f'O ano \033[1;32m{ano}\033[m é bissexto'if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0) else f'O Ano \033[1;31m{ano}\033[m não é bissexto!')