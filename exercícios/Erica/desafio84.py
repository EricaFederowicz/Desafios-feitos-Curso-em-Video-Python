# leia nome e peso de varias pessoas e guarde numa lista
# mostre quantas pessoas foram cadastradas
# as pessoas mais pesadas
# as pessoas mais leves
lista = []
dados = []
cont = 0
maior= 0
menor = 0
nomemenor = 0
nomemaior = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    lista.append(dados[:]) # copiando os dados recebidos para a lista
    dados.clear() # limpando os dados
    cont += 1 # contador para saber quantas pessoas foram cadastradas
    more = str(input('Deseja continuar? S/N ')).upper().strip()[0]
    if more not in 'NS':
        print('Opção inválida. Tente novamente.')
        more = str(input('Deseja continuar? S/N ')).upper().strip()[0]
    elif more == 'N':
        break
print('~'*40)
print(f'Foram cadastradas {cont} pessoas.')
for i in lista:
    if i == lista[0]: #se i for o item 0 da lista
        maior = i[1] # i sera o maior e menor valor
        menor = i[1]
        nomemaior = i[0]
        nomemenor = i[0]
    else: # se i não for o item 0
        if i[1] > maior: # se i for maior que o maior número ele será o novo maior
            maior = i[1]
            nomemaior = i[0]
        if i[1] <= menor: # se i for menor que o menor número ele será o novo menor
            menor = i[1]
            nomemenor = i[0]
print(f'o menor peso foi de {nomemenor} com {menor}kg.')
print(f'O maior peso foi de {nomemaior} com {maior}kg.')
print('FIM')






