#faça um programa que leia um número qualquer e mostre o seu fatorial.
#ex 5! = 5x4x3x2x1 =120
#
num = int(input('Digite um número para saber o fatorial: '))
res = num
while num  > 0:
    if(num > 1):
        print(num, end='x')
        num -= 1
        res = res * num
    else:
        print(num, end='')
        num -= 1
print(f'={res}', end=' ')
#
# # 5x4 = 20
# # 20x3 = 60
# # 60 * 2 = 120
# # 120 * 1 = 120
#
#
# from math import factorial
# n = int(input('Digite um número para calcular o fatorial: '))
# print(f'O fatorial de {n} é {factorial(n)}.')