x = float(input('Largura da parede: '))
y = float(input('Altura da parede: '))

area = x * y

print('Sua parede tem a dimesnsão de {:,.2f}x{:,.2f} e sua área é de {:.2f}m²' .format(x, y, area))
print('Para pintar essa parede, você precisa de {:.2f}l de tinta' .format((area) / 2))
