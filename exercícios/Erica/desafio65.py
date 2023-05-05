# leia um numero inteiro e pergunte ao usuario se ele quer continuar digitando
# no final mostre a média dos numeros digitados, mostre tambem o maior e o menor
print('\033[35m='*30,'\033[m')
print('LEITOR DE NÚMEROS')
print('\033[35m='*30,'\033[m')
n = int(input('\nDigite um número inteiro: '))
more = int(input('\nDeseja continuar?\n\033[35m[1]Sim\033[m \n\033[32m[2]Não\033[m '))
lista = [n]
count = 1
while more == 1:
    n = int(input('\nDigite outro número inteiro: '))
    lista += [n]
    count += +1
    more = int(input('\nDeseja continuar?\n\033[35m[1]Sim\033[m \n\033[32m[2]Não\033[m '))
if more == 2:
    print('\n\033[32mOs números digitados foram:\n{}'.format(lista))
    print('\nA média dos valores é: {:.2f} '.format((sum(lista)/count)))
    print('\nO menor número é {} e o maior é {}'.format(max(lista),min(lista)))
    print('FIM')
else:
    print('\nComando inválido.')
    print('FIM')
    quit()


