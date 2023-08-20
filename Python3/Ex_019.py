import random

alunos = []

for i in range(4):
    alunos.append(input('Nome do {}º aluno: ' .format(i + 1)))

print('O aluno escolhido foi {}' .format(random.choice(alunos)))
