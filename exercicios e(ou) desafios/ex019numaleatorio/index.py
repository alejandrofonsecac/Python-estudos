import random
num = random.randint(1, 4)

print('Tem 4 alunos, os nomes deles são, nesta sequencia: \n Alejandro \n Mateus \n Wesley \n João \n Os escolhidos para limpar o quadro são: ')

if num == 1:
    print('\nAlejandro será o escolhido')
elif num == 2:
    print('\nMateus será o escolhido')
elif num == 3:
    print('\nWesley será o escolhido')
elif num == 4:
    print('\nJoão será o escolhido')