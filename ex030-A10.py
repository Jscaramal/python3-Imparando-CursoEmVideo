#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número inteiro: '))
print(f'O número \033[1;32m{num}\033[m é Par' if num % 2 == 0 else f'O número \033[1;31m{num}\033[m é impar')