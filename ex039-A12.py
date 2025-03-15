#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é hora de se alistar.
# - Se já passou do tempo do alistamento.
from datetime import date
from turtle import delay
from typing import final

# Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.

print('='*20)
print('Exército Brasileiro')
print('='*20)
anoNasc = int(input('Digite o ano do seu nascimento: '))
sexo = str(input('Digite o sexo [M/F]: ')).upper()
if sexo == 'F':
    print('Você mulher não precisa se alistar!!')
    exit("FIM")
print('-'*20)
print('Analisando...')
anoAtual = date.today().year
idade = anoAtual - anoNasc
delay(3)
print('-'*20)
if idade == 18:
    print('Está na hora de se alistar! Você tem {} anos.'.format(idade))
elif idade < 18:
    saldo = 18 - idade
    print('Está chegando o momento! Você tem {} anos faltantes para se alistar!'.format(saldo))
    print(f'Seu alistamento será em {anoAtual + saldo}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você perdeu o prazo! Já se passaram {saldo} anos! Regularize sua situação em uma Junta Militar.')
    print(f'Seu alistamento foi no ano de {anoAtual - saldo}.')

