# gere cinco números aleatórios e coloque-os numa tupla
# depois mostre os números gerados e indique o menor e o maior
from random import randint
numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('\033[32m-'*50,'\033[m')
print(f'Os números sorteados foram: {numeros}')
print('\033[32m-'*50,'\033[m')
menor = min(numeros)
print(f'O menor número sorteado foi: {menor}')
print('\033[32m-'*50,'\033[m')
maior = max(numeros)
print(f'O maior número sorteado foi: {maior}')
print('FIM')

