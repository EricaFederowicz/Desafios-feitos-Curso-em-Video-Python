# receba o nome de uma pessoa e diga se tem Silva no nome
nome = input('Digite seu nome completo: ')
nome1 = nome.lower()
if ('silva') in (nome1): print('Sim, possui Silva')
if ('silva') not in (nome1): print('Não, sem Silva.')