#crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. ´
# No final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.
# alunos = []
# nome = []
# notas = []
# while True:
#     nome.append(str(input('Nome: ')).strip())
#     notas.append(float(input('Nota 1: ')))
#     notas.append(float(input('Nota 2: ')))
#     alunos.append([nome[:], notas[:]])
#     nome.clear()
#     notas.clear()
#     r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
#     if r in 'N':
#         break
# print('-='*30)
# print(f"{'No.':<3}", end='')
# print(f"{'NOME':<10}", end='')
# print(f"{'MÉDIA':<3}")
# print('-'*20)
# for  i in range(len(alunos)):
#     print(f'{alunos.index(alunos[i]):<3}', end='')
#     print(f'{alunos[i][0][0]:<10}', end ='')   
#     print(f'{(alunos[i][1][0] + alunos[i][1][1])/2:<3.1f}') # arrumar alinhamento
# print('-'*20)
# while True:
#     opt = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
#     if opt == 999:
#         break
#     else:
#         if opt >= len(alunos) or opt < 0:
#             print('-'*20)
#             print('ALUNO NÃO ENCONTRADO!')
#             continue
#         print('-'*20)
#         print(f'AS notas de {alunos[opt][0]} são {alunos[opt][1]}')
#         print('-'*20)
# print('FINALIZANDO...')
# print('<<< VOLTE SEMPRE >>>')

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))[0]
    if resp in 'Nn':
        break
print('-'*20)
print('-='*30)
print(f"{'No.':<3}", end='')
print(f"{'NOME':<10}", end='')
print(f"{'MÉDIA':<3}")
print('-'*20)
for i in range(len(ficha)):
    print(f'{ficha.index(ficha[i]):<3}', end='')
    print(f'{ficha[i][0]:<10}', end ='')   
    print(f'{(ficha[i][1][0] + ficha[i][1][1])/2:<3.1f}') # arrumar alinhamento
print('-'*20)
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? Digite 999 para sair. '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha)-1 and opc >= 0:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTe SEMPRE >>>')