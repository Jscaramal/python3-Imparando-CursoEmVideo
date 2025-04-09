# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:  
# a) de 1 até 10, de 1 em 1                                              
# b) de 10 até 0, de 2 em 2                                               
# c) uma contagem personalizada

from os import system
system('cls')

def contagem(inicio, fim, passo):
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1
    if(inicio < fim):
        fim += 1
    else:
        fim -= 1
    for i in range (inicio, fim, passo):
        print(i, end=' ')
    print('FIM')
    print('-='*30)
    
        
contagem(1,10,1)
contagem(10,0,-2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio,fim, passo)