# receba a altura e o peso de uma pesoa e calcule seu imc.
# mostre também seu status.
print('\033[35m='*30,'\033[m')
print('CALCULADOR DE IMC E SAÚDE')
print('\033[35m='*30,'\033[m')
peso = float(input('Digite aqui seu peso em Kg: '))
altura = float(input('Digite aqui sua altura em m: '))
imc = peso/(altura**2)
print('Seu IMC é {:.1f}.'
      .format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso.')
elif 18.9 < imc < 25:
    print('Você está no peso ideal.')
elif 25 < imc < 30:
    print('Você está com sobrepeso.')
elif 30 < imc < 40:
    print('Você está com obesidade.')
elif imc > 40:
    print('Você está com obesidade mórbida.')
    
