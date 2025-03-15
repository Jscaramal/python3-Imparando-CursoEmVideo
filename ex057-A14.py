# leia o sexo de uma pessoa, mas só aceite M ou F. Caso esteja errado, peça a digitação novamente até o valor ser correto.
v = input('Digite sei sexo: [M/F]: ').strip().upper()[0]
while v not in 'FM':
    v = str(input('Dado inválido. Digite o sexo [M/F]: ')).strip().upper()[0]
print(f"Sexo {v.upper()} registrado com sucesso!")