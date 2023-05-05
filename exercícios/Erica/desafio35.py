# receba o comprimento de tres retas e diga se é possivel formar um triangulo
a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))
n = abs(a-b)
m = abs(a-c)
o = abs(b-c)
if o < a < (b+c):
    print('True')
else:
    print('Nao é possivel formar um triangulo com estas medidas')
    quit()
if m < b < (a+c):
    print('True')
else:
    print('Nao é possivel formar um triangulo com estas medidas')
    quit()
if n < c < (a+b):
    print('True')
else:
    print('Nao é possivel formar um triangulo com estas medidas')
    quit()
