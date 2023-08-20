strFrase = input('Digite uma frase: ').upper()

print('A letra A aparece {} vezes na frase' .format(strFrase.count('A')))
print('A primeira letra A aparece na posição {}' .format(strFrase.find('A') + 1))
print('A última letra A aparece na posição {}' .format(strFrase.rfind('A') + 1))
