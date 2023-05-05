# receba tres numeros e diga qual o maior e o menor
a = int(input('Digite um número: '))
b = int(input('Digite outro: '))
c = int(input('Mais um: '))
lista = [a,b,c]
print(lista)
print('O maior número é {}'.format(max(lista)))
print('O menor número é {}'.format(min(lista)))
