# leia o nome, a idade e o sexo de 4 pessoas e mostre:
# a média de idade do grupo
# o nome do homem mais velho
# quantas mulheres tem menos de 20 anos
print('\033[35m='*30,'\033[m')
print('ANALISADOR DE GRUPO')
print('\033[35m='*30,'\033[m')
lista_nome_feminino = [] # lista para receber os dados imputados
lista_idade_feminino = []
lista_sexo = []
lista_nome_masculino = []
lista_idade_masculino = []
for _ in range(1,5):
    sexo = input('Qual o sexo da {}° pessoa? \n[1] Masculino \n[2] Feminino '.format(_))
    if sexo == '1': #se o sexo for masculino as informaçoes vão para lista masculina
        nomem = input('\nQual o nome da {}° pessoa? '.format(_))
        idadem = input('\nQual a idade da {}° pessoa? '.format(_))
        lista_nome_masculino += [nomem]
        lista_idade_masculino += [int(idadem)]
    if sexo == '2': #se o sexo for feminino as informaçoes vão pra lista feminina
        nomef = input('\nQual o nome da {}° pessoa? '.format(_))
        idadef = input('\nQual a idade da {}° pessoa? '.format(_))
        lista_nome_feminino += [nomef]
        lista_idade_feminino += [int(idadef)]
    else:
        print('Opção inválida, não aceitamos pessoas trans neste programa.')
        quit()
lista_idade = lista_idade_masculino + lista_idade_feminino #juntando as idades masculinas e femininas em uma lista
media_idade = sum(lista_idade)/4 # fazendo a media de idade
print('\nA média de idade do grupo é {} anos.'.format(media_idade))
maior_idade_masculina = max(lista_idade_masculino) #descobrindo a maior idade masculina
loc_maior_idade_masculina = lista_idade_masculino.index(maior_idade_masculina) #localização da maior idade masculina
print('\nO homem mais velho é o {}, com {} anos.'.format(lista_nome_masculino[loc_maior_idade_masculina],maior_idade_masculina)) #igualando a posiçao da maior idade masculina com a lista de nomes masculinos
menorq20 = 20 #para filtrar a lista de idade feminina
filtro_lista = [c for c in lista_idade_feminino if c < menorq20] #nova lista que apresenta apenas os itens da lista de idade feminina que são menores que 20
print('\nA quantidade de mulheres com menos de 20 anos é {}.'.format(len(filtro_lista))) # quantidade de itens na nova lista de idades abaixo de 20
print('\nFIM')










