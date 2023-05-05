# façao computador jogar par ou impar com o usuario, parando apenas quando o jogador perder
# no fim mostre o total de vitórias do jogador
print('\033[32m='*30,'\033[m')
print('PAR OU ÍMPAR')
print('\033[32m='*30,'\033[m')
from random import randint
count = 0
while True:
    jogador = int(input('Qual número quer jogar? '))
    escolhajog = str(input('Par ou Ímpar? [P]/[I] ')).upper().strip()[0]
    while escolhajog not in 'PpIi':
        escolhajog = str(input('Par ou Ímpar? [P]/[I] ')).upper().strip()[0]
    computador = randint(0, 10)
    soma = jogador + computador
    if soma % 2 == 0:
        print(f'{soma} é Par.')
        if escolhajog == 'P':
            count += 1
            print('-' * 30)
            print(f'Parabéns, você ganhou!')
            print('-' * 30)
        if escolhajog == 'I':
            print('-' * 50)
            print('Não foi dessa vez. Mais sorte na próxima.')
            print(f'Você ganhou {count} vezes.')
            print('-' * 50)
            break
    if soma % 2 != 0:
        print(f'{soma} é Ímpar.')
        if escolhajog == 'I':
            count += 1
            print('-'*30)
            print(f'Parabéns, você ganhou!')
            print('-'*30)
        if escolhajog == 'P':
            print('-' * 50)
            print('Não foi dessa vez. Mais sorte na próxima.')
            print(f'Você ganhou {count} vezes.')
            print('-' * 50)
            break
print('FIM')





