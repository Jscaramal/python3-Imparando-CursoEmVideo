#Leia seis numeros int e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere.

print('Digite 6 números inteiros e eu vou somar os pares.')
numero = 0
cont = 0
for c in range(6):
    n = int(input('Digite o número: '))
    if n % 2 == 0:
        cont += 1
        numero += n
print('Informado {} valores pares. A soma dos pares foram: {}'.format(cont,numero))