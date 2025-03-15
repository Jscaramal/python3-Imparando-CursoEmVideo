#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
# Ex. Digitar um número: 6.127
#O numero 6.127 tem a parte inteira 6.

from math import trunc

numero = float(input('Digitar um número: '))
print('O número {} tem a parte inteira {}.'.format(numero, trunc(numero)))