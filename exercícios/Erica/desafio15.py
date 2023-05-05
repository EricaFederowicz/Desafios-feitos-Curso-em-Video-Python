#pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Informe a quantidade de km rodados: '))
dias = int(input('Informe a quantidade de dias em que usou o carro: '))
vd = dias * 60
vkm = km * 0.15
total = vd + vkm
print('Você usou o carro por {} dias e percorreu {}km. O valor a pagar é de R${:.2f}.'.format(dias, km, total))

