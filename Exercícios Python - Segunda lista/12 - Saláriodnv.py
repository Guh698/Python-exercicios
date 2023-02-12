#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
"""descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.
"""
Vh = float(input("Insira o valor da hora:"))
Ht  = float(input("Insira a quantidade de horas trabalhadas no mês:"))

salario_bruto = Vh * Ht
if salario_bruto <= 900:
    desconto = 0.0
elif salario_bruto > 900 and salario_bruto <= 1500:
    desconto = 5
elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto = 10
else:
    desconto = 20

IR = salario_bruto * (desconto / 100)
INSS = salario_bruto * (10 / 100)
FGTS = salario_bruto * (11 / 100)
Totaldesc = IR + INSS
salario_liquido = salario_bruto - Totaldesc

if salario_bruto <= 2500:
    print(f"\nSalário Bruto     : R${salario_bruto}"
          f"\nTotal de descontos: R${Totaldesc}"
          f"\nSalário Liquido   : R${salario_liquido}")
elif salario_bruto >= 2500:
    print(
    f"\nSalário Bruto     : R${salario_bruto}"
    f"\n(-) IR            : R${IR}"
    f"\n(-) INSS          : R${INSS}"
    f"\nFGTS              : R${FGTS}"
    f"\nTotal de descontos: R${Totaldesc}"
    f"\nSalário Liquido   : R${salario_liquido}")


