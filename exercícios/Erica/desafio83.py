# leia uma expressão entre parenteses e diga se ela é válida
n = str(input('Digite uma expressão com parênteses: '))
lista = list(n)
abrep = lista.count('(')
fechap = lista.count(')')
if abrep == fechap:
    print('A expressão digitada é válida.')
else:
    print('A expressão digitada é inválida.')
print('FIM')
