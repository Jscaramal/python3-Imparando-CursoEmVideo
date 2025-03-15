#faça um programa que leia um número inteiro e diga se ele é ou não um numero primo.
# n = int(input('Digite um numero inteiro: '))
# p = 0
# for c in range(1, n + 1):
#     if n % c == 0:
#         p += 1
# print(f"o numero {n} é PRIMO!" if p == 2 else f"o numero {n} NÃO é PRIMO!" )

n = int(input('Digite um numero inteiro: '))
p = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        p += 1
    else:
        print('\033[m', end='')
    print(c, end=' ')
print(f"\n\033[mO numero {n} é PRIMO!" if p == 2 else f"\n\033[mo numero {n} NÃO é PRIMO!")