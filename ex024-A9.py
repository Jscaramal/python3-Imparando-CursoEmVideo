'''Crie um programa que leia o nome de uma cidade e diga se ela
comça ou não com o nome "SANTO" '''

cidade = str(input('Digite o nome de uma cidade: '))

cidade = cidade.title().split()
print(cidade)
print('A cidade começa com "Santo" ?')
print('Santo' in cidade[0])