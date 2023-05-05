#leia um número n e mostre os n primeiros numeros da sequencia de fibonatti
print('\033[35m='*30,'\033[m')
print('SEQUENCIA DE FIBONACCI')
print('\033[35m='*30,'\033[m')
qnt = int(input('Quantos números da sequência deseja ver? '))
n0 = 0
n1 = 1
print('1',end='  ')
for _ in range(qnt-1):
    n = n0 + n1
    n0 = n1
    n1 = n
    print(n,end='  ')
print('FIM')


