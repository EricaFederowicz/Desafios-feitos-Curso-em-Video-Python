#  leia 7 valores e os guarde numa unica lista separando pares de impares
# mostre pares e impares de forma crescente
lista = [[],[]]
for _ in range(7):
    n = int(input(f'Digite o {_+1}° número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('~'*40)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares foram:{lista[0]}')
print(f'Os valores ímpares foram:{lista[1]}')
print('FIM')




