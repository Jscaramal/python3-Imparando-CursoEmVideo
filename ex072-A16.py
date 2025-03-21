# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numerais = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
              'dez', 'onze', 'doze', 'treze', 'quatorze',
               'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if not 0 <= num <= 20:
        print('Tente novamente. ', end='')
    else:
        print(f'Você digitou o número {numerais[num]}')
        while True:
            c = str(input('Quer continuar? [S/N] ')).strip().upper()
            if c not in 'SN':
                print('Tente novamente. ', end='')
            else:
                break
        if c == 'N':
            break
        elif c == 'S':
            continue
print('Fim do programa.')