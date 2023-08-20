x = []

for i in range(3):
    x.append(int(input('Digite o {}º valor: ' .format(i + 1))))

x.sort()

print('O menor valor digitado é {}' .format(x[0]))
print('O maior valor digitado é {}' .format(x[2]))
