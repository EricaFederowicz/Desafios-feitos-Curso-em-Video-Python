# leia o sexo de uma pessoa e só aceite os valores F e M, caso receba outro valor peça a digitação novamente até
# ter o valor correto
sexo = 'c' # precisa já ter a variável que o while usará, o valor atrelado a ela nesse caso não importa
while sexo not in ['M','F']: # para mais de um elemento o != não funcionou, precisei fazer uma lista
    sexo = (input('Qual seu sexo? [M] ou [F]: ')).upper()
print('FIM')



