# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00
"""
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
a - comprar apenas latas de 18 litros;
b - comprar apenas galões de 3,6 litros;
c - misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""


m = metrosQ = float(input("R:"))
latas = 0
galões = 0

while metrosQ > 108:
    metrosQ -= 108
    latas += 1
if metrosQ > 0 and metrosQ <= 108:
    latas += 1

print(f"Para {m}m² é necessário apenas {latas} latas de tinta, pagando {latas *80}R$")

metrosQ = m
while metrosQ > 21.6:
    metrosQ -= 21.6
    galões += 1
if metrosQ > 0 and metrosQ <= 21.6:
    galões += 1

print(f"Para {m}m² é necessário apenas {galões} galões de tinta, pagando {galões *25}R$")

metrosQ = m
latas = 0
galões = 0
while metrosQ > 108:
    metrosQ -= 108
    latas += 1
while metrosQ > 21.6:
    metrosQ -= 21.6
    galões += 1
if metrosQ > 0 and metrosQ <= 21.6:
    galões += 1    
       
print(f"Para {m}m² é necessário apenas {latas, galões} galões e latas  de tinta, pagando {(galões*25) + (latas*80)}R$")
