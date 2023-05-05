# receba a velocidade de um carro e se for acima de 80 km/h diga que ele foi multado.
#  a multa vai custar 7 reais a cada km/h acima do limite

velocidade = int(input('Qual a velocidade? '))
if velocidade > 80:
    print('Você está acima do limite permitido, haverá multa.')
    print('A multa será de R${} .'.format((velocidade-80)*7))
else:
    print('Você está dentro do limite de velocidade permitido.')