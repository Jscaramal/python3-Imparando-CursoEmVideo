# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - média abaixo de 5.0: REPROVADO
# - média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
from turtle import delay

print('=-'*20)
print('Será que você passou de ano?')
print('=-'*20)
n1 = float(input('Eu vou calcular para você. Digite sua primeira nota: N1 = '))
n2 = float(input('Digite sua segunda nota: N2 = '))
m = (n1 + n2) / 2
print('Calculando...')
delay(3)
print('-'*20)
print('...')
delay(3)
if m >= 7.0:
    print(f'APROVADO! Com uma média muito boa de {m:.1f}')
elif 5.0 < m < 7.0:
    print(f"RECUPERAÇÃO! Com uma média mediocre de {m:.1f}")
else:
    print(f"REPROVADO! Com uma média lamentável de {m:.1f}")