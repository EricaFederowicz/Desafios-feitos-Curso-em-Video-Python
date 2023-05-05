# 4 jogadores jogam um dado e recebem valores aleatórios
# guarde os resultados num dicionário e mostre em ordem do maior para o menor
from random import randint
from time import sleep
dados = {}
dados['jogador_1'] = randint(1,6)
dados['jogador_2'] = randint(1,6)
dados['jogador_3'] = randint(1,6)
dados['jogador_4'] = randint(1,6)

for k,v in dados.items():
    print(f'{k} recebeu o valor {v}')
print('='*45)


for k,v in dados.items():
    if k == 'jogador_1':
        maior = menor = segmaior = v
        pos1 = 'jogador_1'
        pos2 = 'jogador_1'
        pos3 = 'jogador_1'
        pos4 = 'jogador_1'
    if k == 'jogador_2':
        if v > maior:
            maior = v
            pos1 = k
        elif v < menor:
            menor = v
            pos4 = k
        elif v >= menor and v <= maior:
            segmaior = v
            pos2 = k
            pos3 = k
    if k == 'jogador_3':
        if v > maior:
            maior = v
            pos1 = k
        if v < menor:
            menor = v
            pos4 = k
        if v >= segmaior:
            segmaior = v
            pos2 = k
        if v <= segmaior:
            pos3 = k
    if k == 'jogador_4':
        if v > maior:
            maior = v
            pos1 = k
        if v < menor:
            menor = v
            pos4 = k
        if v >= segmaior:
            segmaior = v
            pos2 = k
        if v <= segmaior:
            pos3 = k


print(f'ganhador: {pos1}\n'
      f'2° lugar: {pos2}\n'
      f'3° lugar: {pos3}\n'
      f'4° lugar: {pos4}')
print('FIM')






