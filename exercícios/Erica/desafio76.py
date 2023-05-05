# crie uma tupla como nomes de produtos e seus preços ao lado. depois motre em forma de tabela.
produtos = ('Tablet', 3500.00, 'Luz Colante', 5.00, 'Airbuds plus', 600.00, 'Bolsa', 100.00, 'Cadeira de Escritório', 300.00)
print('\033[32m-'*40,'\033[m')
print('{:^40}'.format('TABELA DE PREÇOS'))
print('\033[32m-'*40,'\033[m')
prod = 0
preço = 1
for _ in range(5):
    print('{:.<30}'.format(produtos[prod]),end='')
    print('R${: >8.2f}'.format(produtos[preço]))
    prod += 2
    preço += 2
print('\033[32m-'*40,'\033[m')
print('FIM')



