# leia um número entre 0 e 20 e mostre ele escrito por extenso.
print('\033[33m='*30,'\033[m')
print('NÚMERO POR EXTENSO')
print('\033[33m='*30,'\033[m')
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('De 0 á 20.Qual número deseja ver? '))
while n < 0 or n > 20:
    n = int(input('Número inválido.Tente novamente.\n'
                  'De 0 á 20.\nQual número deseja ver?'))
print('\033[33m-'*30,'\033[m')
print(f'Você digitou o número {extenso[n]}')
print('\033[33m-'*30,'\033[m')
print('FIM')



