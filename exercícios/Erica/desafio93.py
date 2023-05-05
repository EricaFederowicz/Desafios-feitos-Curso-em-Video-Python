# leia o nome de um jogador, a qnt de partidas jogadas e a quantidade de gols feitos por partida

dados = {}
gols = []

dados['Nome'] = input('Nome do jogador: ').capitalize()
dados['Partidas_jogadas'] = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))

for _ in range(dados['Partidas_jogadas']):
    n = int(input(f'Quantos gols {dados["Nome"]} fez na {_+1}° partida? '))
    gols += [n]

dados['gols'] = gols[:]
dados['total'] = sum(gols)

print('\n','='*45)
for k,v in dados.items():
    print(f'{k} tem valor {v}')

print('\n','='*45)
print(f'O jogador {dados["Nome"]} jogou {dados["Partidas_jogadas"]} partidas.')

for p,i in enumerate(gols):
    print(f'* Na partida {p}, {dados["Nome"]} fez {i} gols.')

print(f'Foi um total de {dados["total"]} gols')
print('FIM')










