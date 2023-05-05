# leia um número e converta para binário, octal e hexadecimal
print('\033[35m='*30,'\033[m')
print('CONVERSOR NUMÉRICO')
print('\033[35m='*30,'\033[m')
print('''Opções de conversão:
      [1] BINÁRIO 
      [2] OCTAL 
      [3] HEXADECIMAL.''')
escolha = int(input('Digite o número correspondente a conversão desejada: '))
if escolha > 3:
    print('Opção inválida bundão.')
    quit()
numero = int(input('Digite o número que deseja converter: '))
if escolha == 1:
    print('O número {} convertido para base Binária é {}'
          .format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O número {} convertido para base Octal é {}'
          .format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O número {} convertido para base Hexadecimal é {}'
          .format(numero, hex(numero)[2:]))


