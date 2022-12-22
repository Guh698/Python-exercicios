# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
""" a - Para homens: (72.7*h) - 58
    b - Para mulheres: (62.1*h) - 44.7 """

h = float(input("Insira sua altura:"))
g = str(input("Insira seu gênero:"))

g = g.upper()
g = g.replace(" ", "")

if g == "HOMEM" or g == "H":
    print("\nSeu peso ideal é:", (72.7*h) - 58)
elif g == "MULHER" or g == "M":
    print("\nSeu peso ideal é:", (62.1*h) - 44.7)
else:
    print("\nSeu gênero biológico é invalido")