# leia vários números inteiros até que o número 999 seja digitado
# mostre quantos números foram digitados e a soma deles
print('\033[35m='*30,'\033[m')
print('PARA PARAR DIGITE 999')
print('\033[35m='*30,'\033[m')
n = int(input('Digite um número inteiro: '))
lista = [n]
cont = 1
soma = 0
while True:
    n = int(input('Digite outro número: '))
    if n == 999:
        break
    lista += [n]
    cont += 1
    soma += n
print(f'Você digitou {cont} números e a soma deles é {soma}.')
print('FIM')



