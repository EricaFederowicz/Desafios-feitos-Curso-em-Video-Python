# leia 6 números inteiros e mostre a soma apenas dos pares, desconsidere os ímpares.
print('\033[35m='*30,'\033[m')
print('SOMADOR DE NÚMEROS PARES')
print('\033[35m='*30,'\033[m')
soma = 0
for numero in range (0, 6): #repita o comando abaixo 6 vezes
    numero = int(input('Escolha um número: '))
    if (numero % 2 == 0): # se o número lido for divisível por 2 (se for par)
        soma += numero # a cada numero par lido some ao resultado anterior
        print('A soma dos valores pares é {}'.format(soma))
print('FIM')


