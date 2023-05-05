# leia o peso de 5 pessoas e diga qual o maior e o menor peso.
print('\033[35m='*30,'\033[m')
print('LEITOR DE PESO')
print('\033[35m='*30,'\033[m')
lista = [] # criei a lista para armazenar os pesos, se não ele não guarda os valores
for _ in range (1,6):
    peso = input('Qual o peso da {}° pesoa? Kg '.format(_)) #usei format para ele mostar a posição da pessoa
    lista += [peso] #cada peso informado vai ser adicionado á lista
print(lista)
print('O maior peso é {}'.format(max(lista))) # comando max() mostra o maior item da lista
print('O menor peso é {}'.format(min(lista))) # comando min() mostra o menor item da lista
print('FIM')





