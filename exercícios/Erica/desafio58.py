# melhore o desafio 28. O computador vai pensar num número de 0 á 10 e o jogador vai tentar adivinhar
# o jogador vai adivinhar até acertar e no fim o computador vai mostrar quantos palpites foram necessários
print('\033[35m='*30,'\033[m')
print('GUESS THE NUMBER. FROM 0 TO 10')
print('\033[35m='*30,'\033[m')
from random import randint
tries = 1 # variable to count how many times the user guesses
n = randint(0,10) # randint picks a number ramdonly between the given interval
guess = int(input('I just thought on a number from 0 to 10 with my iron brain, can u guess what was the number? '))
while guess != n: # while guess not equal n it will loop
    if guess > n:
        print('Maybe a little less...')
    if guess < n:
        print('Maybe a little more...')
    guess = int(input('Try again: '))
    tries += +1 # at each guess we count plus 1
if guess == n:
    print('\nCongrats dear, I really thought number {} '.format(n))
    print('It only took you {} attempts'.format(tries))
print('FIM')






