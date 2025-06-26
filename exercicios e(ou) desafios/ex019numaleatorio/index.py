import random
num = random.randint(1, 4)

a1 = str(input('Escolha o nome do 1 aluno para limpar o quadro: '))
a2 = str(input('Escolha o nome do 2 aluno para limpar o quadro: '))
a3 = str(input('Escolha o nome do 3 aluno para limpar o quadro: '))
a4 = str(input('Escolha o nome do 4 aluno para limpar o quadro: '))

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f'O escolhido será: {escolhido}')