# leia o nome de uma cidade e diga se começa ou não com o nome "Santo"
nome = str(input('Qual o nome da cidade? '))
nome1 = nome.lower()
separado = nome1.split()
primeirapalavra = separado[0]
if str('santo') in (primeirapalavra): print('Sim, o nome da cidade começa com Santo.')
if str('santo') not in (primeirapalavra): print('Não, o nome da cidade não começa com Santo.')




