# leia dois valores e mostre um menu na tela [1]somar [2]multiplicar [3]maior [4]novos numeros [5]sair do programa
print('\033[35m='*30,'\033[m')
print('DOIS NÚMEROS')
print('\033[35m='*30,'\033[m')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
opçao = int(input('\n\033[32m[1] Somar\033[m'
                  '\n\033[34m[2] Multiplicar\033[m'
                  '\n\033[35m[3] Maior\033[m'
                  '\n\033[33m[4] Novos números\033[m'
                  '\n\033[31m[5] Sair do programa\033[m'
                  '\nEscolha sua opção:'))
while opçao != 5:
    if opçao == 0:
        print('\n\033[31mOpção inválida, escolha novamente.\033[m')
        opçao = int(input('\n\033[32m[1] Somar\033[m'
                          '\n\033[34m[2] Multiplicar\033[m'
                          '\n\033[35m[3] Maior\033[m'
                          '\n\033[33m[4] Novos números\033[m'
                          '\n\033[31m[5] Sair do programa\033[m'
                          '\nEscolha sua opção:'))
    if opçao == 1:
        soma = n1 + n2
        print('\n\033[32mA soma dos números {} e {} é {}'.format(n1, n2, soma))
        opçao = int(input('\n\033[32m[1] Somar\033[m'
                          '\n\033[34m[2] Multiplicar\033[m'
                          '\n\033[35m[3] Maior\033[m'
                          '\n\033[33m[4] Novos números\033[m'
                          '\n\033[31m[5] Sair do programa\033[m'
                          '\nEscolha sua opção:'))
    if opçao == 2:
        multiplicaçao = n1 * n2
        print('\n\033[34mA multiplicação dos números {} e {} é {}'.format(n1, n2, multiplicaçao))
        opçao = int(input('\n\033[32m[1] Somar\033[m'
                          '\n\033[34m[2] Multiplicar\033[m'
                          '\n\033[35m[3] Maior\033[m'
                          '\n\033[33m[4] Novos números\033[m'
                          '\n\033[31m[5] Sair do programa\033[m'
                          '\nEscolha sua opção:'))
    if opçao == 3:
        if n1 > n2:
            print('\n\033[35mO número {} é maior que {}'.format(n1, n2))
        if n2 > n1:
            print('\n\033[35mO número {} é maior que {}'.format(n2, n1))
        if n2 == n1:
            print('\n\033[35mOs dois números digitados são iguais.')
        opçao = int(input('\n\033[32m[1] Somar\033[m'
                          '\n\033[34m[2] Multiplicar\033[m'
                          '\n\033[35m[3] Maior\033[m'
                          '\n\033[33m[4] Novos números\033[m'
                          '\n\033[31m[5] Sair do programa\033[m'
                          '\nEscolha sua opção:'))
    if opçao == 4:
        n1 = float(input('\n\033[33mDigite o primeiro número: '))
        n2 = float(input('\033[33mDigite o segundo número: '))
        opçao = int(input('\n\033[32m[1] Somar\033[m'
                          '\n\033[34m[2] Multiplicar\033[m'
                          '\n\033[35m[3] Maior\033[m'
                          '\n\033[33m[4] Novos números\033[m'
                          '\n\033[31m[5] Sair do programa\033[m'
                          '\nEscolha sua opção:'))
    if opçao > 5:
        print('\n\033[31mOpção inválida, escolha novamente.\033[m')
        opçao = int(input('\n\033[32m[1] Somar\033[m'
                          '\n\033[34m[2] Multiplicar\033[m'
                          '\n\033[35m[3] Maior\033[m'
                          '\n\033[33m[4] Novos números\033[m'
                          '\n\033[31m[5] Sair do programa\033[m'
                          '\nEscolha sua opção:'))
if opçao == 5:
    print('\nFIM')









