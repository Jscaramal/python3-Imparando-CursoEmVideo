#leia nome, idade e sexo de 4 pessoas. no final do programa, mostre:
# A média de idade do grupo.
# Nome do Homem mais velho.
# Quantas mulheres tem menos de 20 anos
qtdPessoas = 4
nomeHomemMaisVelho = ""
idadeHomemMaisVelho = 0
mediaDeIdade = 0
qtdMulheres = 0

for c in range(1, qtdPessoas + 1):
    nome = str(input('Digite o nome da pessoa {}: '.format(c)))
    idade = int(input('Digite o idade da pessoa {}: '.format(c)))
    sexo = str(input('Digite M ou F para o sexo da pessoa {}: '.format(c)))
    print('=-'*10)
    if sexo in 'Mm':
        if idade > idadeHomemMaisVelho:
            nomeHomemMaisVelho = nome
            idadeHomemMaisVelho = idade
    elif sexo in 'Ff':
        if idade < 20:
            qtdMulheres += 1
    else:
        print('Não existe esse sexo! Erro!')
    mediaDeIdade += idade

mediaDeIdade = mediaDeIdade / qtdPessoas

print("="*20)
print(f"O nome do homem mais velho é {nomeHomemMaisVelho} com a idade de {idadeHomemMaisVelho} anos.")
print(f"A quantidade de mulheres abaixo de 20 anos é {qtdMulheres}.")
print(f"A média de idade do grupo é de {mediaDeIdade :.1f} anos.")

