x = input('digite algo, qualquer coisa.')
print('\033[35mqual o tipo?', type(x))
print('\033[31msó tem letras?', x.isalpha())
print('\033[32msó tem números?', x.isnumeric())
print('\033[33mtem letras e números?', x.isalnum())
print('\033[34mé maiúsculo?', x.isupper())
print('\033[36mé minúsculo?', x.islower())
print('\033[37mestá capitalizado?', x.istitle())
print('\033[35mé só espaço?', x.isspace())


