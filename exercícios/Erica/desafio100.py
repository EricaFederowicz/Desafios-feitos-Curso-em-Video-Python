from random import randint
from time import sleep

numeros = []

def sorteia(list):
    print('Foram sorteados os números:')
    for i in range(5):
        n = randint(1,100)
        numeros.append(n)
        sleep(0.5)
        print(n,end=' ')
    print('\n ')


sorteia(numeros)

def somaPar(list):
    print('A soma dos números pares é:',end=' ')
    soma = 0
    for i in list:
        if i % 2 == 0:
            soma += i
    sleep(0.5)
    print(soma)


somaPar(numeros)

print('FIM')



