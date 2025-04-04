# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, 
# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
# além da idade, com quantos anos a pessoa vai se aposentar.
from os import system
from datetime import datetime

def limpar_console():
    system('cls')
limpar_console()

worker  = {
    "nome": str(input('Nome: ')),
    "nascimento": int(input('Ano de Nascimento: ')),
    "Carteira De Trabalho": int(input('Carteira de Trabalho (0 não tem): '))
}
year = datetime.now().year
worker['idade'] = year - worker.pop('nascimento')
if worker['Carteira De Trabalho'] != 0:
    worker.update({
        "Ano de Contratação": int(input('Ano de Contratação: ')),
        "Salário": float(input('Salário: R$')),
    })
    worker["Aposentadoria"] = (worker['Ano de Contratação'] + 35) - year + worker['idade']
print('-='*30)
for k, v in worker.items():
    print(f' - {k} tem o valor {v}')