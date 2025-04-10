from os import system
from time import sleep
system('cls')

def analisador(*num):
    quantidade = len(num)
    if len(num) == 0:
        maior = 0
    else:
        maior = max(num)
    print('-='*30)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n}', end=' ')
        sleep(0.5)
    print(f'Foram informados {quantidade} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


analisador(3,4,5)
analisador()