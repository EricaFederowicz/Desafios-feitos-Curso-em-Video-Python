# calcule o valor de um produto de acordo com seu preço normal e a forma de pagamento
print('\033[35m='*30,'\033[m')
print('CALCULADOR DE PREÇO FINAL')
print('\033[35m='*30,'\033[m')
preço = float(input('Qual o preço normal do produto? R$ '))
print('Formas de pagamento disponíveis: Dinheiro, Cartão até 3x, Pix.')
pagamento = input('Qual será a forma de pagamento? ').upper().strip()
desconto10 = preço - (preço*(10/100))
desconto5 = preço - (preço*(5/100))
juros20 = preço + (preço*(20/100))
if pagamento == 'DINHEIRO':
    print('Por pagar em Dinheiro você receberá 10% de desconto.\nO valor a ser pago é de \033[35mR${:.2f}'
          .format(desconto10))
elif pagamento == 'CARTAO A VISTA' or 'CARTAO 1X' or 'CARTAO1X' or 'CARTAO UMA VEZ' or 'CARTAOUMAVEZ':
    print('Por pagar com Cartão a vista você receberá 5% de desconto.\nO valor a ser pago é de \033[35mR${:.2f}'
          .format(desconto5))
elif pagamento == 'CARTAO 2X' or 'CARTAO2X' or 'CARTAO DUAS VEZES' or 'CARTAODUASVEZES':
    print('Por pagar com Cartão em duas parcelas você pagará o valor normal.\nTotal a pagar \033[35mR${:.2f}'
          .format(preço))
elif pagamento == 'CARTAO 3X' or 'CARTAO3X' or 'CARTAO TRES VEZES' or 'CARTAOTRESVEZES':
    print('Por pagar com Cartão em três parcelas você terá o acréscimo de 20% de juros.\nO total a pagar é de \033[35mR${:.2f}'
          .format(juros20))
elif pagamento == 'PIX':
    print('Por pagar com Pix você terá 10% de desconto.\nO total a pagar é de \033[35mR${:.2f}'
          .format(desconto10))


