#Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário , com 15% de aumento.

salario = float(input('Inserisci il tuo stipendio attuale:€'))
nuovoSalario = salario + (salario * 0.15)
print('Tuo nuovo stipendio è €{:.2f}'.format(nuovoSalario))