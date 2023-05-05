# crie uma matriz 3x3
# mostre a soma dos valores pares
# a soma dos valores da terceira coluna
# o maior valor da segunda linha
matriz = [[],[],[],
          [],[],[],
          [],[],[]]
pares = []
for i in range(len(matriz)):
    n = int(input(f'Digite um número para a posição {i}: '))
    matriz[i].append(n)
    if n % 2 ==0:
        pares += [n]
print(matriz[:3])
print(matriz[3:6])
print(matriz[6:])
print('='*30)
print(f'A soma dos valóres pares é: {sum(pares)}')
tercolun = matriz[2::3]
somatercolun = [tercolun[0][0],tercolun[1][0],tercolun[2][0]]
print(f'A soma da terceira coluna é: {sum(somatercolun)}')
segunlinha = matriz[3:6]
maiorsegundalinha = [segunlinha[0][0],segunlinha[1][0],segunlinha[2][0]]
print(f'O maior valor da segunda linha é: {max(maiorsegundalinha)}')
print('FIM')



