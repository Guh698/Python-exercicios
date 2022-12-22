# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
""" a - o produto do dobro do primeiro com metade do segundo.
    b - a soma do triplo do primeiro com o terceiro.
    c - o terceiro elevado ao cubo. """


Na = int(input("Insira o primeiro número inteiro:"))
Nb = int(input("Insira o segundo número inteiro:"))
Nr = float(input("Insira o número real:"))

print("\na - o produto do dobro do primeiro com metade do segundo:", Na*2 + Nb/2)

print("\nb - a soma do triplo do primeiro com o terceiro:", Na*3 + Nr*3)

print("\nc - o terceiro elevado ao cubo:", Nr**3)