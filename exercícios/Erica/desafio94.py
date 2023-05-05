# leia nome idade e sexo de varias pessoas guardando os dados de cada uma em um dicionário e todos os dicionários numa lista
# no fim mostre quantas pessoas foram cadastradas, a media de idade do grupo, uma lista com todas as mulheres
# e uma lista com todas a pessoas de idade acima da média

dados = {}
lista = []

while True:
    dados['Nome'] = input('Nome: ').capitalize()
    dados['Idade'] = int(input('Idade: '))
    dados['Sexo'] = input('Sexo: F/M ').upper()[0]

    lista += [dados.copy()]

    del(dados['Nome'])
    del(dados['Idade'])
    del(dados['Sexo'])

    more = input('Deseja continuar? S/N ').upper()[0]

    while more not in 'SN':
        more = input('Deseja continuar? S/N ').upper()[0]
    if more == 'N':
        break

print(lista)
print('\033[32m='*60,'\033[m')
print(f'\n* Foram cadastradas {len(lista)} pessoas.')

idades = []
for i in range(len(lista)):
    idades += [lista[i]['Idade']]

media = (sum(idades)) / len(lista)
print(f'\n* A média das idades é {media:.2f}.')

count = 0
mulheres = []
for i in range(len(lista)):
    if lista[i]['Sexo'] == 'F':
        count += 1
        mulheres += [lista[i]['Nome']]

print(f'\n* A quantidade de mulheres cadastradas é {count}.')
print('     E seus nomes são: ')
print(mulheres)

velhos = []
for i in range(len(lista)):
    if lista[i]['Idade'] > media:
        velhos += [lista[i]['Nome']]

print(f'\n* A quantidade de pessoas com idade acima da média é : {len(velhos)}.')
print('     E seus nomes são: ')
print(velhos)

print('FIM')










