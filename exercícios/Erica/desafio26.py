# receba uma frase e diga quantas vezes aparece a letra A, em qual posição aparece pela primeira e pela ultima vez
frase = input('Digite uma frase: ')
minusculo = frase.lower()
print('A letra A aparece {} vezes'.format(minusculo.count('a')))
if ('a') not in (minusculo): quit()
print('A letra A apareceu pela primeira vez na posição: ', end='')
print(minusculo.find('a'))
print('A letra A aparece pela última vez na posição: ', end= '')
print(minusculo.rfind('a'))




