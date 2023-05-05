def escreva(txt):
    t = len(txt)+4
    print('\033[32m='*t,'\033[m')
    print(f'  {(txt)}')
    print('\033[32m='*t, '\033[m')


escreva('Olá Mundo!')

print('FIM')




