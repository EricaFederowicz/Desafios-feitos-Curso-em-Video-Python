# simule o funcionamento de um caixa eletronico, pergunte ao usuario qual sera o valor sacado
# e informe quantas cédulas serão entregues
# cédulas de 50, 20, 10 e 1
print('\033[34m='*30,'\033[m')
print('{:^30}'.format('BANCO KITYCAT'))
print('\033[34m='*30,'\033[m')
print('\nBem vindo ao Banco KityCat!')
saque = int(input('Qual o valor que deseja sacar? R$'))
notas50 = 0
notas20 = 0
notas10 = 0
notas1 = 0
print('\033[34m-'*30,'\033[m')
print('Serão sacadas:')
while saque >= 50:
    saque -= 50
    notas50 += 1
while saque >= 20:
    saque -= 20
    notas20 += 1
while saque >= 10:
    saque -= 10
    notas10 += 1
while saque >= 1:
    saque -= 1
    notas1 += 1
if notas50 > 0:
    print(f'{notas50} notas de R$50,00')
if notas20 > 0:
    print(f'{notas20} notas de R$20,00')
if notas10 > 0:
    print(f'{notas10} notas de R$10,00')
if notas1 > 0:
    print(f'{notas1} notas de R$1,00')
print('\033[34m-'*30,'\033[m')
print('\nObrigada pela preferência, volte sempre!')
print('FIM')

















