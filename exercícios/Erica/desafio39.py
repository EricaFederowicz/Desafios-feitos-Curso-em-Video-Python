# Leia o ano de nascimento de uma pessoa e informe se ainda vai se alistar, se está na hora ou se já passou do tempo.
# Informe tambem quanto tempo ainda falta ou quanto já passou se for o caso.
import datetime
print('\033[35m='*30)
print('\033[mANALISADOR DE ALISTAMENTO')
print('\033[35m=\033[m'*30)
anonascimento = int(input('Qual seu ano de nascimento? '))
sexo = str(input('É menino ou é menina? '))
hoje = datetime.date.today()
anoatual = int(hoje.year)
idade = int(anoatual - anonascimento)
if sexo == 'menina':
    print('Querida, não se preocupe com isso. Vai estudar pra ser girl boss.')
    quit()
elif idade > 18:
    print('Voce já tem {} anos, já deveria ter se alistado a {} anos atrás.'
          .format(idade, (idade-18)))
elif idade < 18:
    print('Voce ainda não chegou na idade para alistamento. Faltam {} anos para poder se alistar.'
          .format(18-idade))
elif idade == 18:
    print('Voce está na idade de fazer o alistamento. Boa sorte!')





