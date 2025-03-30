#crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
#
# Exemplo de expressão: (a+b) * (c+d)
# Exemplo de expressão: (a+b) * (c+d
# Exemplo de expressão: (a+b) * c+d)
# Exemplo de expressão: a+b) * (c+d)

exp = str(input('Digite uma expressão: '))
l1 = []
l2 = []
for c in exp:
    if c == '(':
        l1.append(c)
    if c == ')':
        l2.append(c)

while len(l1) != 0 and len(l2) != 0:
    l1.remove('(')
    l2.remove(')')
        
if len(l1) == 0 and len(l2) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')