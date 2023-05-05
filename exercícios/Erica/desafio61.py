# refaça o desafio 51 usando while.
# leia o primeiro termo de uma PA e a razão e mostre os 10 primeiros termos
print('\033[35m='*5,'\033[m')
print('PA')
print('\033[35m='*5,'\033[m')
t = int(input('Qual o primeiro termo da P.A? '))
r = int(input('Qual a razão? '))
cont = 0
while cont < 10:
    cont += +1
    pa = t + (r*cont)
    print(pa-r)
print('FIM')

