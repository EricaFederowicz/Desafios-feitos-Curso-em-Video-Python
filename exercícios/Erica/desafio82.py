# leia vários numeros e os coloque numa lista
# crie outras duas listas com os valores pares e os valores ímpares
lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista += [n]
    if n % 2 == 0:
        par += [n]
    else:
        impar += [n]
    more = input('Deseja continuar? S/N ').upper().strip()[0]
    if more not in 'SN':
        print('Comando inválido.')
        more = input('Deseja continuar? S/N ').upper().strip()[0]
    if more == 'N':
        break
print(f'Os valores digitados foram:{lista}')
print(f'Os valores pares foram:{par}')
print(f'Os valores ímpares foram: {impar}')
print('FIM')

