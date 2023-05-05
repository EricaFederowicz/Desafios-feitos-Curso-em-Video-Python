# faça uma contagem regressiva de 0 a 10 com 1 segundo de espera a cada numero.
print('\033[35m='*30,'\033[m')
print('CONTAGEM REGRESSIVA REVEILOM')
print('\033[35m='*30,'\033[m')
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[35mFELIZ ANO NOVO!!!')
