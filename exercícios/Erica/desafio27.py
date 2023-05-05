# receba o nome completo de uma pessoa e mostre o primeiro e o ultimo nome
nome = input('Digite aqui seu nome completo: ')
separado = nome.split()
print('Primeiro nome: ', end='')
print(separado[0])
print('Ultimo nome: ', end='')
print(separado[-1])
