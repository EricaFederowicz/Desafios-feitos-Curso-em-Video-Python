# receba um valor em metros e transforme em cm e mm
n = float(input('Qual o valor em metros que deseja converter?'))
print('{} metros é equivalente a {:.0f}cm e a {:.0f}mm.'.format(n, n*100, n*1000))
