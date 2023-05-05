# leia o nome e o preço de vários produtos perguntando se o usuário deseja continuar
# no fim mostre o gasto total
# qnts produtos custam mais q 100 reais
# qual o nome do produto mais barato
nomes = []
preços = []
while True:
    print('\033[35m-\033[m' * 30)
    nome = input('Insira o nome do produto: ')
    preço = float(input('Insira o valor do produto: R$'))
    nomes += [nome]
    preços += [preço]
    print('\033[35m-\033[m'*30)
    more = input('[S]/[N]\nDeseja inserir outro produto? ').upper().strip()[0]
    if more not in 'SN':
        more = input('[S]/[N]\nDeseja inserir outro produto? ').upper().strip()[0]
    if more == 'N':
        print('\033[35m-\033[m' * 30)
        gasto = sum(preços)
        print(f'O total foi de R${gasto:.2f}')
        maisq100 = len([p for p in preços if p > 100])
        print(f'\n{maisq100} produtos custaram mais que R$100,00')
        posiçao_menor_valor = preços.index(min(preços))
        print(f'\nO item mais barato foi {nomes[posiçao_menor_valor]} que custou R${min(preços):.2f}')
        print('\033[35m-\033[m' * 30)
        break
print('FIM')


