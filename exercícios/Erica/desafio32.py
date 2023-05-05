# receba um ano e diga se ele é bissexto
ano = int(input('Digite um ano: '))
resto = ano % 4
if resto == 0:
    print('O ano digitado é bissexto.')
else:
    print('O ano digitado não é bissexto.')

