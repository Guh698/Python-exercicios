# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

V = float(input("Insira um valor:"))

if V > 0:
    print(f"{V} é um valor positivo")
elif V == 0:
    print(f"{V} é um valor nêutro")
else:
    print(f"{V} é um valor negativo")
