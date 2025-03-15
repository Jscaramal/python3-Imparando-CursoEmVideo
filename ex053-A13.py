# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase que verei se é um palíndromo (ex: apos a sopa): '))
flimpa = frase.upper()
flimpa = flimpa.replace(' ', '')
#print("A frase é um palíndrom" if flimpa == flimpa[::-1] else "NAO")
# for c in range(len(flimpa), 0, -1 ):
#     print(flimpa[::-1])
#
# print(flimpa)
fcontr = ""
for c in range(len(flimpa)-1, -1 , -1):
    fcontr += flimpa[c]
if fcontr == flimpa:
    print(f'A palavra {flimpa} è igual a {fcontr}')
else:
    print(f'A palavra {flimpa} NÃO è igual a {fcontr}')
