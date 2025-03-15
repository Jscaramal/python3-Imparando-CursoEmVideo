# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonnacci

n = int(input('Digite o numero inteiro qualquer que vou mostrar a sequencia de fibonnacci: '))
a = 0
b = 1
c = 2

print(f'F(0) = {a}')
print(f'F(1) = {b}')
while  c < n+1:
    p = a + b
    print(f'F({c}) = {p}')
    c += 1
    a, b = b, p
