# refaça o desafio 35 agora especificando qual tipo de triangulo será formado.
# equilatero = todos os lados iguais
# isosceles = dois lados iguais
# escaleno = todos os lados diferentes
print('\033[35m='*30,'\033[m')
print('ANALISADOR DE TRIÂNGULOS')
print('\033[35m='*30,'\033[m')
a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))
n = abs(a-b)
m = abs(a-c)
o = abs(b-c)
if o < a < (b+c):
    print('.')
else:
    print('Nao é possivel formar um triangulo com estas medidas')
    quit()
if m < b < (a+c):
    print('.')
else:
    print('Nao é possivel formar um triangulo com estas medidas')
    quit()
if n < c < (a+b):
    print('Com estes comprimentos de reta é possível formar um triangulo')
else:
    print('Nao é possivel formar um triangulo com estas medidas')
    quit()
if a == b and b == c:
    print('O triangulo formado por estas retas seria equilátero.')
elif a == b and b != c:
    print('O triangulo formado por estas retas seria isósceles.')
elif c == b and c != a:
    print('O triangulo formado por estas retas seria isósceles.')
elif a == c and b != c:
    print('O triangulo formado por estas retas seria isósceles.')
elif a != c and a != b and c != b:
    print('O triangulo formado por estas retas seria escaleno.')
print('FIM')
