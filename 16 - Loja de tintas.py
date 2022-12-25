# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

m = metrosQ = float(input("R:"))
latas = 0
while metrosQ > 54:
    metrosQ -= 54
    latas += 1
if metrosQ > 0 and metrosQ <= 54:
    latas += 1
print(f"Para {m}m de parede, será necessario de {latas} latas, tendo o valor total de R${latas * 80}")