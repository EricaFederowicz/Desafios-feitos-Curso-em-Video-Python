# crie uma função chamada área q receba largura e altura de um terreno e diga sua área

def area(altura,largura):
    r = altura * largura
    print(f'A área do seu terreno {altura}x{largura} é de {r} m².')


def linha():
    print('\033[32m='*45,'\033[m')


linha()
print(f'{"AREA CALCULATOR": ^45}')
linha()

a = int(input('Digite a altura em metros: '))
b = int(input('Digite a largura em metros: '))

area(a,b)

print('\nFIM')











