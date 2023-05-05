# receba o valor da casa, o valor do salário e a quantidade de anos para o pagamento
# o valor da parcela não pode ultrapassar 30% do valor do salário
print('='*30)
print('SIMULADOR DE EMPRÉSTIMO')
print('='*30)
valorcasa = int(input('Qual o valor do imóvel? R$ '))
salario = int(input('Qual seu salário bruto? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))
tempo = anos*12
valorparcela = valorcasa/tempo
parcelamaxima = salario*(30/100)
if valorparcela > parcelamaxima:
    print('\nInfelizmente o empréstimo não poderá ser concedido nessas condições.\n'
          'O valor máximo de parcela equivale á 30% do salário.')
else:
    print('Nessas condições, o valor de parcela será \033[35mR${:.2f}'.format(valorparcela))
    

