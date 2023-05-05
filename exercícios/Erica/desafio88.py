# ajude um jogador da mega sena a criar palpites
# pergunte quantos jogos o usuario quer, a cada jogo sorteie 6 números de 1 á 60 sem repetição
# cadastre tudo em uma lista composta
from time import sleep
from random import randint
sorteados = []
palpites = int(input('Quantos palpites deseja receber? '))
palpite = []
count = 0
print('Os valores gerados foram:')
sleep(1)
for _ in range(palpites):
    for p in range(6):
        palpite.append(randint(0,60))
    sorteados = palpite[:]
    palpite.clear()
    print(f'{_+1}° palpite: {sorteados}')
    sleep(1)
print('Boa Sorte!')
print('FIM')





