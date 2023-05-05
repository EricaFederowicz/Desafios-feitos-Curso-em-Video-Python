#leia um número e diga se ele é ou não um número primo(divisível apenas por 1 e por ele mesmo)
print('\033[35m='*30,'\033[m')
print('RECONHECEDOR DE PRIMOS')
print('\033[35m='*30,'\033[m')
n = int(input('Qual número deseja testar? '))
if n == 2 or n == 3 or n == 7 or n ==5:
    print('O número é primo.')
elif n == 1:
    print('O número não é primo')
elif n % 2 == 0:
    print('O número não é primo')
elif n % 3 == 0:
    print('O número não é primo.')
elif n % 5 == 0:
    print('O número não é primo.')
elif n % 7 ==0:
    print('O número não é primo.')
else:
    print('O número é primo.')
