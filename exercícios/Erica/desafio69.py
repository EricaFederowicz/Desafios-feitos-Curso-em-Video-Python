# leia a idade e o sexo de várias pessoas perguntando se o usuário deseja continuar
# no fim mostre quantas pessoas tem mais de 18 anos
# quantos homens foram cadastrados
# quantas mulheres tem menos de 20 anos
idademulheres = []
idades = []
homens = 0
while True:
    print('\033[32m=' * 30, '\033[m')
    idade = int(input('Informe a idade da pessoa: '))
    sexo = input('[M]/[F]\nInforme o sexo da pessoa: ').upper().strip()[0]
    idades += [idade]
    if sexo == 'F':
        idademulheres += [idade]
    if sexo == 'M':
        homens += 1
    if sexo not in 'FM':
        sexo = input('[M]/[F]\nInforme o sexo da pessoa: ').upper().strip()[0]
    print('\033[32m=' * 30, '\033[m')
    more = input('[S]/[N]\nDeseja continuar? ').upper().strip()[0]
    if more == 'N':
        maior18 = len([i for i in idades if i > 18])
        print('\033[32m=' * 30, '\033[m')
        print(f'Tem {maior18} pessoas com mais de 18 anos.')
        print(f'\nTem {homens} homens no grupo.')
        menor20 = len([i for i in idademulheres if i < 20])
        print(f'\nTem {menor20} mulheres com menos de 20 anos no grupo.')
        break
    if more not in 'SN':
        more = input('[S]/[N]\nDeseja continuar? ').upper().strip()[0]
print('FIM')





