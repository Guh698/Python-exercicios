# salário bruto e descontos

a = float(input("Insira quanto você ganha por hora:"))
b = float(input("Insira quantas horas você trabalhou neste mês:"))

rb = a*b

print("\nA - O seu salário bruto neste mês é:", rb)

INSS = (8/100) * rb

print("\nB - Valor descontado do seu salário para o INSS é:", INSS)

Sind = (5/100) * rb
print("\nC - O valor descontado para o sindicato é:", Sind)

desc = Sind + INSS

sl = rb - desc

print("\nD - O seu salário líquido é:", sl)