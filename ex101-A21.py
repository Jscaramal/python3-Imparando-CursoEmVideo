#Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
# OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(anoNascimento):
    from datetime import date
    idade = date.today().year - anoNascimento
    print(f'A idade é {idade}')
    print(f'Com {idade} anos: ', end='')
    if (16 <= idade < 18) or (idade > 65):
        print('VOTO OPCIONAL!')
    elif idade >= 18:
        print('VOTO OBRIGATÓRIO!')
    else:
        print('NÃO VOTA')
    

print('-'*30)
anoNascimento = int(input('Em que ano você nasceu? '))

voto(anoNascimento)
