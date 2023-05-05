# receba duas notas de um aluno e calcule sua média informando se foi aprovado, reprovado ou se está de recuperação.
# abaixo de 5.0 reprovado, entre 5.0 e 6,9 recuperaçao, acima de 6,9 aprovado.
print('\033[35m='*30)
print('\033[mSIMULADOR DE MÉDIAS')
print('\033[35m=\033[m'*30)
n1 = float(input('Qual foi a nota da primeira prova? '))
n2 = float(input('Qual foi a nota da segunda prova? '))
media = (n1+n2)/2
if media < 5.0:
    print('\nDesculpe querido, mas infelizmente sua média foi {} e você está reprovado.\nDevia ter estudado mais, que pena.'
          .format(media))
elif 5.1 <= media <= 6.9:
    print('\nTenho uma notícia boa e uma ruim.\nA ruim é que sua média é {} e você está de recuperação.\nA boa é que você não foi reprovado direto. yeeeey.'
          .format(media))
elif media >= 7.0:
    print('\nParabéns querido! Você está aprovado, sua média foi {} e você não fez mais que sua obrigação.'
          .format(media))
