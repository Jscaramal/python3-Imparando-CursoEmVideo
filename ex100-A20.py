#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from os import system
from time import sleep
from random import randint
system('cls')
def sorteia(numeros):
    print("Sorteando 5 valores da lista: ", end='')
    for i in range (5):
        numeros.append(randint(0,10))
    for n in numeros:
        print(f'{n}', end=' ')
        sleep(0.2)
    print('PRONTO!')    
    
def somaPares(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')
    
numeros = [] 
sorteia(numeros)
somaPares(numeros)
            
    



#somaPares(numeros)
