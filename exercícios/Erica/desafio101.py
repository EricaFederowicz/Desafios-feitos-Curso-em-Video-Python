from datetime import datetime

def voto(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: Voto negado!'
    if idade > 16 and idade < 18:
        return f'Com {idade} anos: Voto opcional!'
    if idade >= 18:
        return f'Com {idade} anos: Voto obrigatório!'
    if idade > 65:
        return f'Com {idade} anos: Voto opcional!'


n = int(input('Em que ano voce nasceu? '))
print(voto(n))

print('FIM')



