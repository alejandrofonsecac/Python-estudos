import random
ordem = random.randint(1, 2)

aluno1 = input('Insira o nome do 1 aluno: ')
aluno2 = input('\nInsira o nome do 2 aluno: ')
aluno3 = input('\nInsira o nome do 3 aluno: ')
aluno4 = input('\nInsira o nome do 4 aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(lista)
