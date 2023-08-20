strNome = input('Digite seu nome completo: ')

strPriNome = strNome[0:strNome.find(' ')]

print('Maiúscula: {}' .format(strNome.upper()))
print('Minúscila: {}' .format(strNome.lower()))
print('Seu nome tem: {} letras' .format(len(strNome) - strNome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras' .format(strPriNome, len(strPriNome)))
