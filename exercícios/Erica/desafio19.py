#receba 4 nomes e escolha um aleatoriamente
import random
n1 = (input('Insira o nome do primeiro aluno: '))
n2 = (input('Insira o nome do segundo aluno: '))
n3 = (input('Insira o nome do terceiro aluno: '))
n4 = (input('Insira o nome do quarto aluno: '))
x = (n1, n2, n3, n4)
y = random.sample(x, 1)
print('O aluno escolhido foi {}'.format(y))


from random import choice
n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
x = choice(lista)
print('O aluno escolhido foi: {}'.format(x))