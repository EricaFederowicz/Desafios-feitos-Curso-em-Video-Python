# receba o preço de um produto e informe seu novo preço com 5% de desconto.
v = float(input('Informe o valor atual do produto: R$'))
print('calculando...')
x = v*(5/100)
y = v-x
print('O valor com desconto é de R${:.2f}'.format(y))
