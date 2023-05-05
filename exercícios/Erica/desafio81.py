# leia vários valores e os coloque numa lista
# mostre quantos números foram digitados
# os valores em ordem decrescente
# se o valor 5 está na lista e quantas vezes foi digitado
lista = []
more = 'S'
count = 0
while True:
    n = int(input('Digite um número: '))
    lista += [n]
    if n == 5:
        count += 1
    more = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if more == 'N':
        break
    if more not in 'SN':
        print('Comando inválido.')
        more = input('Deseja continuar? [S/N] ').upper().strip()[0]
print('\033[32m~'*30,'\033[m')
print(f'Foram digitados {len(lista)} números')
inverso = lista.sort(reverse=True)
print(f'\nOs valores em ordem decrescente são: {lista[::1]}')
if count > 0:
    print(f'\nO número 5 foi digitado {count} vezes.')
if count == 0:
    print(f'\nO valor 5 não foi digitado.')
print('\nFIM')
