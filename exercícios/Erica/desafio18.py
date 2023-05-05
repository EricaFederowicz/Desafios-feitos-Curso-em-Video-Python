# leia um angulo e mostre na tela o valor do seno, cosseno e tangente.
import math
print('Seno, cosseno e tangente de um ângulo')
a = int(input('Insira um ângulo: '))
x = math.radians(a)
print('Para o ângulo {}'.format(a))
print('O Cosseno é: {:.3f}'.format(math.cos(x)))
print('O Seno é: {:.3f}'.format(math.sin(x)))
print('A Tangente é: {:.3f}'.format(math.tan(x)))
print('Eu devia ter tido isso na época da escola!')

from math import radians, cos, sin, tan
a = int(input('Digite o angulo: '))
x = radians(a)
print('O valor do seno é: {:.3f}'.format(sin(x)))
print('O valor do cosseno é: {:.3f}'.format(cos(x)))
print('O valor da tangente é: {:.3f}'.format(tan(x)))


