# receba o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas
# o nome com todas as letras minusculas
# quantas letras tem, sem considerar os espaços
# quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: '))
n_espaços = nome.count(' ')
n_total = len(nome)
n_letras = (n_total)-(n_espaços)
separado = nome.split()
pn = len(separado[0])
print('Em letras maiúsculas: ', end='')
print(nome.upper())
print('Em letras minúsculas: ', end='')
print(nome.lower())
print('Quantidade de letras: ', end='')
print(n_letras)
print('Quantidade de letras do primeiro nome: ')
print(pn)






