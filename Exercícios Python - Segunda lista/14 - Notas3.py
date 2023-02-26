#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
"""  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E"""
 

nota1 = int(input("Insira sua primeira nota:"))
nota2 = int(input("\nInsira sua segunda nota:"))

Media = (nota1 + nota2) /2


if Media >= 9 and Media < 10:
    Mf = "A"
elif Media >= 7.5 and Media < 9:
    Mf = "B"
elif Media >= 6 and Media < 7.5:
    Mf = "C"
elif Media >= 4 and Media < 6:
    Mf = "D"
elif Media >= 0 and Media < 4:
    Mf = "E"
else:
    print("Insira o valor correto de suas notas")

if Media >= 6:
    status = "Aprovado"
elif Media < 6:
    status = "Reprovado"

print(f"A média de suas notas {nota1} e {nota2} é: {Media}; {status}")

input()