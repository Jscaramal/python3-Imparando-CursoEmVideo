'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiusculas
O nome com todas minusculas
quantas letras ao todo (sem considerar expaços)
quantas letras tem o primeiro nome.
'''
nomeCompleto = str(input('Digite seu nome completo: '))
print('Seu nome em maiúsculas é: {}'.format(nomeCompleto.upper()))
print('Seu nome em minúscolas é: {}'.format(nomeCompleto.lower()))
print('Seu nome completo tem {} caracteres' .format(len(nomeCompleto.replace(' ', ''))))
nome = nomeCompleto.split()
print('O seu primeiro nome é {} e contem {} caracteres.'.format(nome[0],len(nome[0])))
