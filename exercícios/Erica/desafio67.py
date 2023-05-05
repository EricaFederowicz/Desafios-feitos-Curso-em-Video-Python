# leia um número e mostre sua tabuada, continue lendo até que leia um número negativo
print('\033[35m='*30,'\033[m')
print('TABUADA INFINITA')
print('PARA PARAR DIGITE  N° NEGATIVO')
print('\033[35m='*30,'\033[m')
while True:
    print('-'*30)
    n = int(input('\nDe qual número deseja ver a tabuada? '))
    if n < 0:
        break
    for c in range (11):
            print(f'{n} x {c} = {n*c}')
print('-'*30)
print('\n\033[32mPrograma encerrado.')
print('FIM')


