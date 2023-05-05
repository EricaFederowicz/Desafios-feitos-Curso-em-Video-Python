# leia varios numeros inteiros e pare quando receber o numero 999
# mostre a soma dos numeros digitados desconsiderando 999
# mostre também quantos números foram digitados
print('\033[35m='*30,'\033[m')
print('PARA PARAR DIGITE 999')
print('\033[35m='*30,'\033[m')
print('\nATENÇÃO! O número de parada 999 não será incluído a contagem nem á soma final.')
n = int(input('\nDigite um número inteiro: '))
lista = [n]
count = 0 # começa com zero para desconsiderar o 999
while n != 999:
    n = int(input('Digite outro número inteiro: '))
    lista += [n]
    count += +1
print('Você digitou {} números antes de 999.'.format(count))
lista.pop()
print('\nOs números digitados foram:\n{}'.format(lista))
print('\nA soma deles é {}'.format(sum(lista)))

