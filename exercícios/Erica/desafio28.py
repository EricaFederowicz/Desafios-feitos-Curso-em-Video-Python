# faça o computador escolher um número entre 0 e 5 e que o usuário tente adivinhar qual foi o número escolhido
# o computador devera dizer se o usuário acertou ou não

import random
lista = [0,1,2,3,4,5]
n = random.sample(lista, 1)
guess = int(input('Qual número entre 0 e 5 acha que foi o escolhido? '))
if n == guess:
    print('Parabens, voce acertou!')
else:
    print('Poxa, não foi dessa vez!')
    print('o número escolhido foi {}.'.format(n))

