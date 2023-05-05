# leia um número qualquer e mostre seu fatorial
print('\033[35m='*10,'\033[m')
print('FATORIAL')
print('\033[35m='*10,'\033[m')
n = int(input('Digite um número: '))
fatorial = n
cont = 1
while n != 1: #enquanto for diferente de um porque se for até 0 ele vai zerar o fatorial
    n = n - 1 # a cada vez q for executado ele vai usar o antecessor de n
    fatorial = fatorial * n # o fatorial então vai ser multiplicado pelo antecessor de n a cada execução
    cont += +1 # usei o contador para depois mostrar o n original
    print(n+1,end='') # vai mostrar na tela os n de cada execução, começando pelo original
    print('x',end='')
print('1') # como o while para no 1 tive que mostrar ele manualmente
print('\nO fatorial do número {} é {}'.format(cont, fatorial))



