#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão:
# -1 para binário
# -2 para octal
# -3 para hexadecimal


print('Vou calcular um número para Binário, Octal ou Hexadecimal')
numero = int(input('Insira um número: '))
escolha = int(input('Insira 1 para converter para binário, 2 para octal ou 3 para hexadecimal. Caso queria sair digite 0:\n - '))
if escolha == 1:
    numero = bin(numero)
    print(numero[2:])
elif escolha == 2:
    numero = oct(numero)
    print(numero[2:])
elif escolha == 3:
    numero = hex(numero)
    print(numero[2:])
else:
    print('Ok! Até Mais');
