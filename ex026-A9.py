''' Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra 'A'.
Em que posição ela aparece a primeira vez
Em que posição ela aparece a ultima vez
'''

frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper()
print(frase)
num = frase.count('A')
print(num)
print('Quantidade de A: {}' .format(frase.find('A')))
print('O primeiro \"A\" aparece na posição: {}'.format(frase.find('A')+1))
print('O ultimo \"A\" aparece na posição: {}'.format(frase.rfind('A')+1))