#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# para salários superiores a R$1250,00, calcule um aumento de 10%
# para os inferiores ou iguais, aumento de 15%

salario = float(input('Digite o seu salario: '))
print(f'O novo salário com 10% é \033[1;32m R$ {salario  + (salario * 10 / 100):.2f}.\033[m' if salario > 1250.00
      else f'O novo salário com 15% de aumento é \033[1;32m R$ {salario + (salario * 15 / 100):.2f}\033[m.')