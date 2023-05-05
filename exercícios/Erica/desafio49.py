# faça a tabuada usando estrutura de repetição.
print('\033[35m='*30,'\033[m')
print('TABUADA')
print('\033[35m='*30,'\033[m')
n = int(input('De qual número deseja ver a tabuada? '))
tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in tabuada:
    print('{} x {}= {}'.format(numero, n, numero*n))
print('FIM')



