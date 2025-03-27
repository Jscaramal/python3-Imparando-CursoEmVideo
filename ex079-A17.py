# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = []
while True:
    v = int(input('Digite um valor: '))
    if(v in valores):
        print('Valor já existe! Não será adicionado.')
    else:
        valores.append(v)
    controle = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if(controle == 'N'):
        break

print('=-' * 30)
print(f'Você digitou os valores {sorted(valores)}')
