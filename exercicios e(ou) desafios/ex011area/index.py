print('Me diga o valor de altura e comprimento que lhe direi a área da parede')
print('Também lhe direi quantos litros de tinta serão necessários')
print('Levando em consideração que 1 litro cobre 2 m²\n')

n1 = float(input('Comprimento (em metros): '))
n2 = float(input('Altura (em metros): '))

area = n1 * n2
tinta = area / 2

print(f'\nA parede tem {area:.2f} m² de área.')
print(f'Você precisará de {tinta:.2f} litros de tinta para pintá-la.')
