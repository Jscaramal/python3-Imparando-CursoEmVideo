#Crie um algoritmo que leia um número e mostre o seu dobro, tripo e raiz quadrada.

num = int(input('Scegli un numero perfavore: '))
print('Ecco il numero scelto {}.'.format(num))
print('Il doppio è {}'.format(2 * num))
print('Il triplo è {}'.format(3 * num))
#print('La radice quadrata è {:.2f}'.format(num ** (1/2)))
print('La radice quadrata è {:.2f}'.format(pow(num, (1/2))))
print('Ciao!')