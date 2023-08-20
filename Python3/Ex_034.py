x = float(input('Digite o salário do funcionário: '))

print('O funcionário que ganhava R${:,.2f}, passa a ganhar R${:,.2f} agora' .format(x, x * 1.1 if(x > 1250) else x * 1.15))
