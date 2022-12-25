# peso max de peixes = 50kg = resulta uma multa de 4 reais (por quilo excedente)


p = int(input("Insira o peso de peixes em kg:"))


if p > 50:
    taxa = (50 - p) * 4
    print("O valor da taxa é:", (taxa))
else:
    print("Nenhuma taxa é aplicada")