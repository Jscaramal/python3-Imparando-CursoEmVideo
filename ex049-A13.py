#Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for:
from time import sleep

print('-='*5)
print('\033[4;30;107m TABUADA \033[m')
print('-='*5)
numero = int(input('Escolha um número que te darei a tabuada dele: '))

for c in range(1, 11):
    print(f'\rLOADING: {c*10}%', end="")
    sleep(0.1)
print('\nResultado: ')
for c in range(1, 11):
    print(f' {numero} x {c} = {numero*c}')
    sleep(0.1)
print('fim')
