# receba o nome de 4 alunos e sorteie uma ordem para eles.
import random
n1 = input('Insira o nome do primeiro aluno: ')
n2 = input('insira o nome do segudo aluno: ')
n3 = input('Insira o nome do terceiro aluno: ')
n4 = input('Insira o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
print('A ordem dos alunos será: {}'.format(random.sample(lista, 4)))
# fazer de novo porque esse me deu uma coça
# outra forma de resolver o deafio
import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação dos alunos será: ')
print(lista)








