# receba o valor do salario de um funcionario e diga qual sera o novo salario com o aumento
#  para salarios maiores que 1,250 dar aumento de 10%
# para salarios menores ou iguais a 1,250 dar aumento de 15%

salario = int(input('Qual o valor atual do slário do funcionário? R$ '))
if salario > 1250:
    novo = salario * (10/100)
    print('O novo salário será R$ {}'.format(salario+novo))
else:
    novo1 = salario * (15/100)
    print('O ovo salário será R$ {}'.format(salario+novo1))
    
