# leia 5 valores e os guarde numa lista
# mostre o menor e maior valores e suas posições na lista
lista = []
for _ in range(5):
    n = int(input(f'Escolha um número para a posição {_+1}: '))
    lista.append(n)
print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))+1}')
print(f'O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista))+1}')
print('FIM')


