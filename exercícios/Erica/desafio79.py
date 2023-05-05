# leia vários números e os coloque numa lista, se já tiver o número desconsidere
# no fim mostre todos os valores digitados em ordem crescente
lista = []
more = 'S'
print('\033[32m-'*30,'\033[m')
while more == 'S':
    n = int(input('Digite um número: '))
    if n in lista:
        print('Número já adicionado.')
        n = int(input('Digite outro número: '))
    lista.append(n)
    more = input('Deseja continuar? [S/N]').upper().strip()[0]
    while more not in 'SN':
        print('Comando inválido.Tente de novo.')
        more = input('Deseja continuar? [S/N]').upper().strip()[0]
organizado = sorted(lista)
print('\033[32m-'*30,'\033[m')
print(f'Os valores digitados foram: {organizado}')
print('FIM')


