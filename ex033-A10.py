#Faça um programa que leia três números e mostre qual é o mairo e qual é o meno.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
lista = [n1, n2, n3]
maior = max(lista)
menor = min(lista)

print(f'O numero maior é \033[1;31m{maior}\033[m e o número menor é \033[1;36m{menor}\033[m' )