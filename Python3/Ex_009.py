x = int(input('Digite um número: '))

print('Tabuada do {}' .format(x))

for i in range(11):
    print('{} x {:2} = {}' .format(x, i, x * i))
