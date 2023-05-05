# leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo
# calcume e mostre o comprimento da hipotenusa
import math
co = float(input('Insira o comprimento do Cateto Oposto: '))
ca = float(input('Insira o comprimento do Cateto Adjacente:'))
h2 = math.pow(co, 2)+ math.pow(ca, 2)
h = math.sqrt(h2)
print('O valor da hipotenusa é {}.'.format(h))

#modo alternativo
co = float(input('Insira o comprimento do Cateto Oposto: '))
ca = float(input('Insira o comprimento do Cateto Adjacente: '))
print('A medida da hipotenusa é {}'.format(math.hypot(co, ca)))
