# Faça um Programa que leia três números e mostre-os em ordem decrescente.

N1 = float(input("Insira um número:"))
N2 = float(input("Insira um número:"))
N3 = float(input("Insira um número:"))

list = [N1, N2, N3]

list.sort(reverse=True)

print(list)