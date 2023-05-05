# calcule a soma de todos os números ímpares que são múltiplos de 3 no intervalo de 1 á 500.
print('\033[35m='*30,'\033[m')
print('N° ÍMPARES MÚLTIPLOS DE 3 ATÉ 500')
print('\033[35m='*30,'\033[m')
s = 0
print('Os números ímpares múltiplos de 3 são:')
for c in range (1, 501, 2): # números ímpares de 1 á 500
    if (c % 3) == 0:  # números ímpares de 1 á 500 divisíveis por 3
        s += c  # s = s + c (como s tem o valor 0 ele soma todos os valores de c)
        print(c)
print('A soma de todos esses números é: ',end='')
print(s)
print('FIM')




