# converta a temperatura informada de graus celcius para fahrenheit.
c = float(input('Informe a temperatura em Celcius: '))
f = c*(9/5)+ 32
print('{:.1f}° Celcius corresponde a {:.1f}° Fahrenheit.'.format(c, f))