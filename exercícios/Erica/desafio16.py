# receba um número qualquer e informe somente sua parte inteira.
import math
n = float(input('Digite um número com casas após a vírgula: '))
print('A parte inteira do valor digitado é {}.'.format(math.trunc(n)))

# segundo modo de resolução
from math import trunc
n = float(input('Digite um número com casas após a vírgula: '))
print('A parte inteira do valor digitado é {}.'.format(trunc(n)))
