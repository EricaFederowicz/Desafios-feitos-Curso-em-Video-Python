# leia o nome de varios jogadores, a qnt de partidas jogadas e a quantidade de gols feitos por partida
# mostre uma planilha com o detalhamento dos dados

dados_jogadores = {}
dados_totais = []

while True:
    dados_jogadores['Nome'] = input('Nome do jogador: ').capitalize()
    dados_jogadores['Jogos'] = int(input(f'Quantos jogos {dados_jogadores["Nome"]} jogou? '))
    for i in range(dados_jogadores['Jogos']):
        if i == 0:
            dados_jogadores['Gols'] = [int(input(f'Quantos gols {dados_jogadores["Nome"]} marcou no {i+1}° jogo? '))]
        else:
            dados_jogadores['Gols'] += [int(input(f'Quantos gols {dados_jogadores["Nome"]} marcou no {i + 1}° jogo? '))]

    dados_totais += [dados_jogadores.copy()]

    del (dados_jogadores['Nome'])
    del (dados_jogadores['Jogos'])
    del (dados_jogadores['Gols'])


    more = input('Deseja continuar? S/N ').upper()[0]
    while more not in 'SN':
        more = input('Deseja continuar? S/N ').upper()[0]
    if more == 'N':
        break

print('='*60)
print('ind.   Nome',' '*4,'Gols')

for i in range(len(dados_totais)):
    print(f'{i} {dados_totais[i]["Nome"]:^15} {sum(dados_totais[i]["Gols"]):^5}')

print('='*60)
while True:
    n = int(input('\n(999 para parar)\nDigite o índice do jogador que deseja ver o desempenho detalhado: '))
    if n == 999:
        break
    else:
        print('='*60)
        print(f'Nome: {dados_totais[n]["Nome"]}')
        print(f'Quantidades de jogos: {dados_totais[n]["Jogos"]}')

        for p,i in enumerate(dados_totais[n]['Gols']):
            print(f'Gols marcados no {p+1}° jogo: {i}')

print('FIM')





















