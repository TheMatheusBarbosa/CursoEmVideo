x = int(input('Qual a velocidade atual do carro? '))

if(x > 80):
    print('Multado! Você excedeu o limite de velocidade que é de 80Km/h')
    print('Você deve pagar multa de R${:,.2f}' .format((x - 80) * 7))
else:
    print('Tenha um bom dia! Dirija com segurança!')
