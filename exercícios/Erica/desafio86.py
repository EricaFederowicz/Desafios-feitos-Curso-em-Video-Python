# crie uma matriz 3x3
matriz = [[],[],[],
          [],[],[],
          [],[],[]]
for i in range(len(matriz)):
    n = int(input(f'Digite um número para a posição {i}: '))
    matriz[i].append(n)
print(matriz[:3])
print(matriz[3:6])
print(matriz[6:])
print('FIM')
