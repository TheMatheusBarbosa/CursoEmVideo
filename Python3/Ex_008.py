x = int(input('Digite uma distância em Quilômetros: '))

print('Metro(s): {:,.0f}m' .format(x * (10**3)))
print('Centímetro(s): {:,.0f}cm' .format(x * (10**5)))
print('Milímetro(s): {:,.0f}mm' .format(x * (10**6)))
print('Micrômetro(s): {:,.0f}mc' .format(x * (10**9)))
print('Nanômetro(s): {:,.0f}nm' .format(x * (10**12)))
