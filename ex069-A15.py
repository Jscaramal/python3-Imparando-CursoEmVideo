#Crie um programa que leia a idade eo sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) QUantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

maiores = homens = mulheres20 = 0
while True:
    print('-'*22)
    print('CADASTRO DE UMA PESSOA')
    print('-'*22)
    idade = int(input('Idade: '))
    if idade > 18:
        maiores += 1
    sexo = " "
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        if sexo == 'M':
            homens += 1
        elif sexo == 'F' and idade < 20:
            mulheres20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-'*22)
print('FIM DO PROGRAMA')
print('-'*22)
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres20} mulheres com menos de 20 anos.')