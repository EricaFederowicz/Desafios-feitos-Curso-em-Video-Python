# melhore o desafio 61 perguntando se o usuário quer que sejam mostrados mais termos
# o programa encerra quando ele disser que quer mostrar 0 termos
print('\033[35m='*5,'\033[m')
print('PA 2.0')
print('\033[35m='*5,'\033[m')
t = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão? '))
qnt = int(input('Quantos termos da PA quer ver? '))
cont = 1 # já comeca no um pq o usuario ja inseriu o 1° termo
lista = [t] #criei a lista para armazenar os termos da PA e mostra-los depois
print(t,end='  ') # ganbiarra para aparecer o primeiro termo
for _ in range (qnt-1): # para mostrar a quantidade de termos pedida (menos 1 para considerar o primeiro termo)
    pa = t + (r*cont)
    cont += +1
    lista += [pa]
    print(pa,end='  ')
more = int(input('\nDeseja ver mais termos dessa PA? [1]Sim [2]Não: '))
while more == 1:
    qnt = int(input('Quantos termos mais deseja ver? '))
    for _ in range(qnt):
        pa1 = t + (r * cont)
        cont += +1
        lista += [pa1]
    print(lista)
    more = int(input('\nDeseja ver mais termos dessa PA? [1]Sim [2]Não: '))
if more == 2:
    print('\nObrigada por me usar, volte sempre!')
    print('FIM')
    quit()
elif more < 1:
    print('\nOpçao inválida, tente de novo.')
    more = int(input('\nDeseja ver mais termos dessa PA? [1]Sim [2]Não: '))
    while more == 1:
        qnt = int(input('Quantos termos mais deseja ver? '))
        for _ in range(qnt):
            pa1 = t + (r * cont)
            cont += +1
            lista += [pa1]
        print(lista)
        more = int(input('\nDeseja ver mais termos dessa PA? [1]Sim [2]Não: '))
    if more == 2:
            print('\nObrigada por me usar, volte sempre!')
            print('FIM')
            quit()
elif more > 2:
    print('\nOpçao inválida, tente de novo.')
    more = int(input('\nDeseja ver mais termos dessa PA? [1]Sim [2]Não: '))
    while more == 1:
        qnt = int(input('Quantos termos mais deseja ver? '))
        for _ in range(qnt):
            pa1 = t + (r * cont)
            cont += +1
            lista += [pa1]
        print(lista)
        more = int(input('\nDeseja ver mais termos dessa PA? [1]Sim [2]Não: '))
    if more == 2:
        print('\nObrigada por me usar, volte sempre!')
        print('FIM')
        quit()








