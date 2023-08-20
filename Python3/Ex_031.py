x = float(input('Qual a distância da sua viagem? '))

print('Você está prestes a começar uma viagem de {:,.1f}Km' .format(x))

if(x <= 200):
    x = x * 0.5
else:
    x = x * 0.45

print('O preço da sua passagem será de R${:,.2f}' .format(x))
