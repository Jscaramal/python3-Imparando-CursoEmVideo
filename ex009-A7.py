#faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.
print('Ti darò la tabellina di un numero scelto!')
numeroInt = int(input('Scegli un numero intero qualsiasi: '))
print('-'*12)
for i in range(1,11):
    print('{} x {:2} = {}'.format(numeroInt, i, numeroInt * i))
print('-'*12)
print('Ti è piaciuto? Arrivederci!')
