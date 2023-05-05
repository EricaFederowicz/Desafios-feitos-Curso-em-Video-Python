# leia nome e média de um aluno e guarde junto á situação numa biblioteca.
# no fim mostre a estrutura na tela
dados = {}
dados['nome'] = input('Nome do aluno: ').capitalize()
dados['media'] = float(input(f'média do aluno {dados["nome"]}:'))
if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
else:
    dados['situação'] = 'Reprovado'
print('='*40)
for k,v in dados.items():
    print(f'{k} é {v}')
print('FIM')


