# crie uma tupla com várias palavras e mostre suas vogais.
tupla = ('fodeu', 'agora', 'fodeu', 'foi', 'tudo', 'amigos', 'e', 'amigas', 'estevao', 'ferreira')
pos = 0
for _ in range(10):
    print(f'\nA palavra {tupla[pos].upper()} tem as vogais: ',end='')
    separado = list(tupla[pos])
    pos += 1
    for i in separado:
        if i in 'aeiou':
            print(f'{i} ',end='')
print('\nFIM')





