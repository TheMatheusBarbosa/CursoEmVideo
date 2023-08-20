x = []

for i in range(3):
    x.append(float(input('Digite o {}º segmento: ' .format(i + 1))))

x.sort()

print('Os segmentos acima {}PODEM FORMAR um triângulo!' .format('NÃO ' if(x[0] + x[1] <= x[2]) else ''))
