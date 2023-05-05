from time import sleep

def contador(inicio,fim,passo):
    if passo == 0:
        passo += 1
    count = inicio
    if inicio < fim:
        print(' ')
        print('\033[32m=' * 45, '\033[m')
        print(f'Contando de {inicio} á {fim} de {passo} em {passo}.')
        sleep(1)
        print(count, end='...')
        while count < fim:
            count += passo
            print(count,end='...')


    if inicio > fim:
        if passo == 0:
            passo += 1
        print(' ')
        print('\033[32m='*45,'\033[m')
        print(f'Contando de {inicio} á {fim} de {passo} em {passo}.')
        sleep(1)
        count = inicio
        print(count, end='...')
        while count > fim:
            if passo > 0:
                count -= passo
                print(count, end='...')
            if passo < 0:
                count += passo
                print(count, end='...')




contador(1,10,1)
contador(10,0,2)

print('\nFaça sua contagem personalizada!')
i = int(input('Inicio:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
contador(i,f,p)

print('FIM')












