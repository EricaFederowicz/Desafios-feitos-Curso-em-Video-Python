# leia 5 números e os cadastre em uma lista já na ordem crescente.
lista = [int(input('Digite um número: '))]
for _ in range(4):
    n = int(input('Digite outro número: '))
    if _ == 0:
        if n > lista[0]:
            lista.append(n)
        elif n < lista[0]:
            lista.insert(0,n)
    if _ > 0:
        if n < lista[0] :
            lista.insert(0,n)
        elif lista[0] < n < lista[1]:
            lista.insert(1,n)
        elif lista[1] < n < lista[2]:
            lista.insert(2,n)
        elif lista[2] < n < lista[3]:
            lista.insert(3,n)
        elif n > max(lista):
            lista.append(n)
print(f'Os números digitados em ordem crescente é: {lista}')
print('FIM')
















