# leia 4 valores pelo teclado e os guarde numa tupla.
# mostre quantas vezes apareceu o 9
# em qual posição voi digitado o primeiro 3
# quais foram os números pares
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
d = int(input('Digite um número: '))
numeros = (a, b, c, d)
print('\033[32m-'*50,'\033[m')
print(f'Os números digitados foram: {numeros}')
print('\033[32m-'*50,'\033[m')
qnts9 = numeros.count(9)
if qnts9 > 0:
    print(f'Foram digitados {qnts9} números 9.')
else:
    print('Não foi digitado nenhum número 9.')
print('\033[32m-'*50,'\033[m')
qnts3 = numeros.count(3)
if qnts3 > 1:
    pos3 = numeros.index(3)
    print(f'O primeiro número 3 aparece na {pos3+1}° posição.')
elif qnts3 == 1:
    pos3 = numeros.index(3)
    print(f'O único número 3 aparece na {pos3+1}° posição.')
elif qnts3 == 0:
    print('Não foi digitado nenhum 3.')
print('\033[32m-'*50,'\033[m')
pares = [i for i in numeros if i % 2 == 0]
if len(pares) > 0:
    print(f'Os números pares digitados foram: {pares}')
else:
    print('Não foi digitado nenhum número par.')
print('FIM')







