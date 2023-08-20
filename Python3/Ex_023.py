x = int(input('Digite um número ente 0 e 9999: '))

print('Unidade: {}' .format(x % 10))
print('Dezena: {}' .format(int((x % 100) / 10)))
print('Centena: {}' .format(int((x % 1000) / 100)))
print('Milhar: {}' .format(int(x / 1000)))
