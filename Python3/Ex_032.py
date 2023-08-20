x = int(input('Qual ano quer analisar? '))

if(x % 400 == 0):
    print('O ano {} é BISSEXTO' .format(x))
elif(x % 100 == 0):
    print('O ano {} NÃO é BISSEXTO' .format(x))
elif(x % 4 == 0):
    print('O ano {} é BISSEXTO' .format(x))
else:
    print('O ano {} NÃO é BISSEXTO' .format(x))
