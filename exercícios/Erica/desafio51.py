# leia o primeiro termo e a razão de uma PA e mostre os 10 primeiros termos
print('\033[35m='*30,'\033[m')
print('MONTE UMA PA')
print('\033[35m='*30,'\033[m')
t = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão? '))
# pa = [t, t+r, t+2r, t+3r, ..., t+9r, t+10r]
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #a cada vez que o "for" for executado ele vai pegar um item da lista na ordem
for vezes in lista:
    print(t+r*vezes) #o R está sendo multiplicado pelo idem da lista da ordem de execução
print('FIM')









