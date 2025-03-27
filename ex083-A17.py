#crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
#
# Exemplo de expressão: (a+b) * (c+d)
# Exemplo de expressão: (a+b) * (c+d
# Exemplo de expressão: (a+b) * c+d)
# Exemplo de expressão: a+b) * (c+d)

exp = str(input('Digite uma expressão: '))
if exp.count('(') == exp.count(')'):
    print('Expressão válida!')
else:
    print('Expressão inválida!')