# Faça um programa que tenha uma função chamada escreva(), que receba um testo qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#Ex: escreva('Olá, Mundo!')
#saida:
# ~~~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~~~

from os import system
system('cls')

def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    
escreva('THE TEST IS GOOD')
escreva('DA HADOUKEN')