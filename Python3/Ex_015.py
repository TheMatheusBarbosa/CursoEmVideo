d = int(input('Quantos dias alugados? '))
k = int(input('Quantos Km\'s rodados? '))

print('O total a pagar é R${:,.2f}' .format((d * 60) + (k * 0.15)))
