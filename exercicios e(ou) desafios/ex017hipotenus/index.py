from math import sqrt

hipo = 0
x = 0
catop = float(input(print('Insira o cateto oposto do triangulo retangulo')))
catad = float(input(print('Insira o cateto adajacente do triangulo retangulo')))

x = catop**2 + catad**2
hipo = sqrt(x)
print(f'A hipotenusa é: {hipo}')
