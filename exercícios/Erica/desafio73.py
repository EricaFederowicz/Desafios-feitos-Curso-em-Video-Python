# crie uma tupla com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol
# mostre: apenas os 5 primeiros colocados
# os ultimos 4 colocados
# uma lista com os times em ordem alfabetica
# em que posição está o time flamengo
times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atletico-PR', 'Atletico-MG', 'Fortaleza',
         'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO',
         'Avaí', 'Juventude')
print(times)
print('\033[32m-'*30,'\033[m')
print('Os 5 primeiros colocados são:')
for i in times[0:6]:
    print(i)
print('\033[33m-'*30,'\033[m')
print('Os últimos 4 são:')
for i in times[-4:]:
    print(i)
print('\033[34m-'*30,'\033[m')
print('Em ordem alfabética:')
print(sorted(times))
print('\033[35m-'*30,'\033[m')
print('Em qual posição está o Flamengo?')
pos = times.index('Flamengo')
print(f'O Flamengo está na {pos+1}° posição.')
print('FIM')



