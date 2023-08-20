from random import randint

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')

x = randint(0, 5)

y = int(input('Em que número eu pensei? '))

if(x == y):
    print('Você ganhou! Eu pensei no número {}!' .format(x))
else:
    print('Ganhei! Eu pensei no número {} e não no {}!' .format(x, y))
