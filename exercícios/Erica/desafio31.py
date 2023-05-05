# receba a distancia de uma viagem e diga o preço que ira custar
# ate 200 km = 0,50   mais de 200 km = 0,45
distancia = int(input('Quantos km terá sua viagem? '))
if distancia <= 200:
    preço = distancia*0.50
    print('Sua viagem irá custar: R${}'.format(preço))
else:
    preço1 = distancia*0.45
    print('Sua viagem irá custar: R${}'.format(preço1))