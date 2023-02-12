# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

P1 = float(input("Insira o valor do produto:"))
P2 = float(input("Insira o valor do produto:"))
P3 = float(input("Insira o valor do produto:"))

list = [P1, P2, P3]

list.sort(reverse=True)
print(f"O Produto mais barato é: {list[-1]}")