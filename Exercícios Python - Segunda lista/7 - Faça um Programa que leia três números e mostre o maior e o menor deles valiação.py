# Faça um Programa que leia três números e mostre o maior e o menor deles.
N1 = float(input("Insira um número:"))
N2 = float(input("Insira um número:"))
N3 = float(input("Insira um número:"))

list = [N1, N2, N3]

list.sort(reverse=True)
print(f"O maior numero é: {list[0]}")
print(f"O menor numero é: {list[-1]}")


