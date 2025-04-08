# Crie um programa que leia nome. sexo e idade de várias pessoas, guarando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final. mostre:
# A) QUantas pessoas cadastradas
# B) A média de idade.
# c) Uma lista com mulheres.
# d) Uma lista com idade acima da média.
from os import system
system('cls')
galera = []
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        interrompe = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if interrompe in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if interrompe == 'N':
        break
media = soma / len(galera)
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas forma ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p['Nome']}', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['Idade'] > media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end=' ')
        print()
print('<< ENCERRADO >>')
