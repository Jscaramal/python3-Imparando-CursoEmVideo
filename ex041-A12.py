# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# até 9 anos :MIRIM
# até 14 anos :INFANTIL
# até 19 anos :JUNIOR
# até 20 anos :SÊNIOR
# Acima: MASTER
from datetime import date

print('#=#'*10)
print('Confederação Nacional de Natação')
print('#=#'*10)
ano = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
i = atual - ano
print('O atleta tem {} anos.'.format(i))
if i <= 9:
    print('Categoria: MIRIM')
elif i <= 14:
    print('Categoria: INFANTIL')
elif  i <= 19:
    print('Categoria: JUNIOR')
elif  i <= 20:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')