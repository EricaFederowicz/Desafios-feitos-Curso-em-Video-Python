# leia o nome e duas notas de alunos e guarde numa lista composta.
# mostre em lista os alunos e suas médias e permita que o usuário escolha o aluno que quer ver as notas
dados = []
while True:
    aluno = str(input('Aluno: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    dados.append(aluno)
    dados.append(n1)
    dados.append(n2)
    media = (n1 + n2)/2
    dados.append(media)
    continuar = input('Deseja continuar?').upper().strip()[0]
    if continuar == 'N':
        break
    while continuar not in 'SN':
        continuar = input('Deseja continuar?').upper().strip()[0]
print('-'*30)
print('{:^30}'.format('BOLETIM'))
print('-'*30)
print('ind.',' '*5,'Nome',' '*5,'Média')
i = 0
count = 0
while i < len(dados):
    print(count,end='')
    print(f'{dados[i]:^23}',end='')
    print(dados[i+3])
    i += 4
    count += 1
print('-'*30)
while True:
    print('\nDigite o índice do aluno para ver suas notas.\n'
          'Digite 999 para parar.')
    qual = int(input('\nÍndice do aluno: '))
    if qual == 999:
        break
    if qual == 0:
        print(f'\nAluno {dados[qual]} teve as notas {dados[qual+1]} e {dados[qual+2]}')
    if qual > 0:
        n = qual * 4
        print(f'\nAluno {dados[n]} teve as notas {dados[n+1]} e {dados[n+2]}')
print('FIM')














