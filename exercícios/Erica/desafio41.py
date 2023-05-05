# receba o ano de nascimento de um atleta e encaixe ele na classificação correta
# até 9 anos: mirin, até 14 anos: infantil, até 19 anos: junior, até 20 anos: sênior, acima: master.
print('\033[35m='*30)
print('\033[mCATEGORIZADOR DE ATLETAS')
print('\033[35m=\033[m'*30)
import datetime
anonascimento = int(input('Qual seu ano de nascimento? '))
data = datetime.datetime.today()
anoatual = int(data.year)
idade = anoatual - anonascimento
if idade <= 9:
    print('Como você tem {} anos, ficará na categoria MIRIN.'
          .format(idade))
elif 9 < idade <= 14:
    print('Como você tem {} anos, ficará na categoria INFANTIL.'
          .format(idade))
elif 14 < idade <= 19:
    print('Como voce tem {} anos, ficará na categoria JUNIOR.'
          .format(idade))
elif 19 < idade <= 20:
    print('Como você tem {} anos. ficará na categoria SÊNIOR.'
          .format(idade))
elif idade > 20:
    print('Como você tem {} anos, ficará na categoria MASTER.'
          .format(idade))


