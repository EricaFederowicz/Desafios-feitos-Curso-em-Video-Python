# Leia dois numeros inteiros e diga se o primeiro ou o segundo é maior, ou se são iguais
print('-'*30)
print('COMPARADOR DE NÚMEROS')
print('-'*30)
n1 = int(input('Digite um número qualquer: '))
n2 = int(input('Digite um segundo número: '))
if n1 > n2:
    print('O \033[35mprimeiro\033[m número é o \033[35mmaior\033[m.')
elif n2 > n1:
    print('O \033[35msegundo\033[m número é o \033[35mmaior\033[m.')
elif n1 == n2:
    print('Os dois números digitados são \033[35miguais\033[m.')
print('Fim')


