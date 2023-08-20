import random

alunos = []

for i in range(4):
    alunos.append(input('Nome do {}º aluno: ' .format(i + 1)))

random.shuffle(alunos)

print('A ordem da apresentação será {}' .format(alunos))
