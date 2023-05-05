# use a largura e a altura de uma parede para calcular quantos m2 tem e dizer quantos litros de tinta serão
# necessários para pintar a parede
print('='*20, 'Tinta calculator', '='*20)
a = float(input('Quantos metros de altura tem a parede? '))
l = float(input('Quantos metros de largura tem a parede? '))
area = a*l
tinta = area/2
import math
print('A quantidade de litros necessários a comprar para pintar são ', math.ceil(tinta),'litros.')
print('.'*100)
print('A quantidade de tinta apresentada foi arredondada para cima para auxilia-lo no momento da compra.')