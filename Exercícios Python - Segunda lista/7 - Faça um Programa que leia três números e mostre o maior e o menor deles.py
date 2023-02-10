# Faça um Programa que leia três números e mostre o maior e o menor deles.

N1 = int(input("Insira o primeiro número:"))
N2 = int(input("Insira o primeiro número:"))
N3 = int(input("Insira o primeiro número:"))

if N1 > N2 and N1 > N3:
    print(f"\nO número {N1} é o maior")
elif N2 > N1 and N2 > N3:
    print(f"\nO número {N2} é o maior")
else:
    print(f"\n número {N3} é o maior")

if N1 < N2 and N1 < N3:
    print(f"\nO número {N1} é o menor")
elif N2 < N1 and N2 < N3:
    print(f"\nO número {N2} é o menor")
else:
    print(f"\n número {N3} é o menor")
