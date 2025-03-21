#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#Apenas os 5 primeiros colocados.
#Os últimos 4 colocados da tabela.
#Uma lista com os times em ordem alfabética.
#Em que posição na tabela está o time da Chapecoense.

tabela = ("Palmeiras", "Flamengo", "Internacional", "Grêmio", "São Paulo", "Atlético Mineiro", "Athletico Paranaense", "Cruzeiro", "Botafogo", "Santos", "Bahia", "Fluminense", "Corinthians", "Chapecoense", "Ceará", "Vasco da Gama", "Sport", "América Mineiro", "Vitória", "Paraná")

print('-=' * 15)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimos são {tabela[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 15)
print(f'O time da Chapecoense está na {tabela.index('Chapecoense')+1}ª posição da tabela!')