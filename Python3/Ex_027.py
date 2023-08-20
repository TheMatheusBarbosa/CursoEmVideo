strNome = input('Digite seu nome completo: ')

print('Seu primeiro nome é {}' .format(strNome[:strNome.find(' ')]))
print('Seu último nome é {}' .format(strNome[strNome.rfind(' ') + 1:]))
