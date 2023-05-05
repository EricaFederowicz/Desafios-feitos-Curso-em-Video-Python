def ficha(jog='N/I',gols='N/I'):
    if jog == '':
        jog = '(Não informado)'
    if gols == '':
        gols = '(Não informado)'
    print(f'O jogador {jog} fez {gols} gols no campeonato')


j = input('Qual o nome do jogador? ')
g = input('Quantos gols ele fez? ')

ficha(j,g)

print('FIM')



