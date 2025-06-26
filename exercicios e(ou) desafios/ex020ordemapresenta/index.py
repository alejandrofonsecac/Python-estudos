import random
ordem = random.randint(1, 2)

aluno1 = input('Insira o nome do 1 aluno: ')
aluno2 = input('\nInsira o nome do 2 aluno: ')
aluno3 = input('\nInsira o nome do 3 aluno: ')
aluno4 = input('\nInsira o nome do 4 aluno: ')

if ordem == 1:
    print(f'A ordem será: {aluno1}, {aluno2},{aluno3},{aluno4}')
elif ordem == 2:
    print(f'A ordem será: {aluno4}, {aluno3},{aluno2},{aluno1}')
