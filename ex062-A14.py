#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns ptermos. O progrma encerra quando ele disser que quer mostrar 0 termos.

ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA:'))
t = 10
while t != 0:
    c = 1
    while c <= t:
        print(f'{ptermo}', end=" → ")
        ptermo += razao
        c += 1
    print('Pausa...')
    t = int(input('Quer mostrar mais termos? Digite a quantidade ou 0 para sair!:\n'))
print('Fim')