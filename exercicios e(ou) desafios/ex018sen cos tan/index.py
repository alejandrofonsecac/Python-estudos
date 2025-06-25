import math
angulo = float(input('Digite o angulo em graus: '))

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.cos(angulo)

menu = int(input('Qual deseja ver? \n [1]Seno \n[2]Cosseno \n [3]Tangente'))

if menu == 1:
    print(f'O valor de {angulo} em Seno é {seno}')
elif menu == 2:
    print(f'O valor de {angulo} em Cosseno é {cosseno}')
elif menu == 3:
    print(f'O valor de {angulo} na Tangente é {tangente}')