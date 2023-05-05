# leia o ano de nascimento de 7 pessoas e mostre quantas já são maiores de idade.
print('\033[35m='*30,'\033[m')
print('LEITOR DE MAIORIDADE')
print('\033[35m='*30,'\033[m')
import datetime
data = datetime.datetime.today()
anoatual = int(data.year)
maior = 0
menor = 0
for c in range (7):
    anonascimento = int(input('Qual seu ano de nascimento? ')) #vai perguntar 7 vezes
    idade = anoatual - anonascimento # calculando a idade baseado no ano atual
    if idade >= 18: # se for maior ou igual a 18
        print('{} anos é considerado maior de idade no brasil.\n'.format(idade))
        maior += +1 # contador dos maiores de idade: a cada maior de idade será somado 1 ao contador
    if idade < 18:
        print('{} anos é considerado menor de idade no Brasil.\n'.format(idade))
        menor += +1 # a cada menor de idade será contado mais 1
print('Tem {} maiores de idade e {} menores de idade no grupo.'.format(maior, menor))
print('FIM')




