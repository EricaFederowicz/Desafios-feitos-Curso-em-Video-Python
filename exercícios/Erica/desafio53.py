# leia uma frase e diga se ela é igual de trás para frente
print('\033[35m='*30,'\033[m')
print('É PALÍMDROMO?')
print('\033[35m='*30,'\033[m')
frase = input('Digite uma frase qualquer: ').replace(' ','').upper() # usei replace para tirar os espaços
lista = list(frase) # transformei em lista para cada caracter ser analisado separadamente
listacontrario = lista[::-1] # coloquei a lista ao contrário
if lista == listacontrario:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
print('FIM')


