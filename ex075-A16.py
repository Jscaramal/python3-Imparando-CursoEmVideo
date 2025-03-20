# Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# Quantas vezes apareceu o valor 9.
# Em que posição foi digitado o primeiro valor 3.
# Quais foram os números pares.

numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print(f'O valor 3 não foi digitado em nenhuma posição' if numeros.count(3) == 0 else f'O valor 3 foi digitado na posição {numeros.index(3)+1}')
print(f'Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')