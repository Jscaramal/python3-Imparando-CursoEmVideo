# crie um programa que tenha uma tupla com vários palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro');

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='') 
    for l in p:
        print(f'{l} ' if l in "aeiou" else "", end='')