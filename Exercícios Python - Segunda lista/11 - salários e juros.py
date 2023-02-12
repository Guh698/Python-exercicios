# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
"""Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

S = float(input("Insira o seu salário:"))

if S <= 280.00:
    SA = (1.20) * S
    print(f"{SA}")
elif S > 280 and S < 700:
    SA = (1.15) * S
    print(f"{SA}")
elif S > 700 and S < 1500:
    SA = (1.10) * S
    print(f"{SA}")
else: 
    SA = (1.05) * S
    SB = (SA - S)
    print(f"Salário antes do reajuste: {S}; porcentual a ser aplicado: 5%; valor do aumento: {SB}; novo salário, após o aumento: {SA}")