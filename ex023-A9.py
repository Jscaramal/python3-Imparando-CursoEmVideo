'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
digitos separados.
Ex. Digite um númerio: 1834

Unidade: 4
Dezena: 3
Centena: 8
milhar: 1
'''
numero = int((input('Digite um numero de 0 a 9999: ')))
numero = f"{numero:04d}"
print('Unidade: {}'.format(numero[3]))
print('Dezena: {}'.format(numero[2]))
print('Centena: {}'.format(numero[1]))
print('milhar: {}'.format(numero[0]))

numero = str((input('Digite um numero String de 0 a 9999: ')))
numero = numero.zfill(4)
print('Unidade: {}'.format(numero[3]))
print('Dezena: {}'.format(numero[2]))
print('Centena: {}'.format(numero[1]))
print('milhar: {}'.format(numero[0]))

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('milhar: {}'.format(m))