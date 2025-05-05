preco = float(input('Digite o preço da compra: R$ '))
desconto = preco * 0.05
preco_final = preco - desconto

print(f'O valor com 5% de desconto é: R$ {preco_final:.2f}')