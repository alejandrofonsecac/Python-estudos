n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
poten = n1 ** n2
di = n1 // n2
dr = n1 % n2

print(f'Os dois produtos são: {n1} e {n2}.\n A soma dos produtos é {s}, a multiplicação é {m}, a divisão é {d:.2f}, a potencia é {poten}, a divisão inteira é {di}, a divisão com resto é {dr}')

#Para limitar o numero de casas apos a virgula é apenas usar {Variavel:.2f} (limita 2 casas)