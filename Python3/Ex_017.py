import math

x = float(input('Comprimento do cateto oposto: '))
y = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa vai medir {:.2f}' .format(math.sqrt((x**2) + (y**2))))
