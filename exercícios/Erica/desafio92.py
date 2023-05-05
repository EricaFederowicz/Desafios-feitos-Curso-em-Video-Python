# leia nome, ano de nascimento e número da carteira de trabalho. se for 0 n tem ctps
# cadastre a idade da pessoa, caso tenha ctps leia o ano do primeiro trabalho e o salário.
# ao final mostre as informaçoes cadastradas e o ano de aposentadoria
import datetime

dados = {}
hoje = datetime.date.today()
anoatual = int(hoje.year)

dados['nome'] = input('Nome: ').capitalize()
dados['idade'] = anoatual - int(input('Qual seu ano de nascimento? '))
dados['ctps'] = int(input('Qual o número da sua carteira de trabalho? (0 caso não tenha) '))

if dados['ctps'] > 0:
    dados['ano_primeiro_trabalho'] = int(input('Em qual ano começou a trabalhar? '))
    dados['salario'] = int(input('Qual o valor do 1° salário? R$'))
    dados['ano_aposentadoria'] = dados['ano_primeiro_trabalho'] + 35

print('\n')
print('='*45)

for k,v in dados.items():
    print(f'{k} tem valor {v}.')

print('FIM')






