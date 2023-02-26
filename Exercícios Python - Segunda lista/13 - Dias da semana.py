# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

Dia = int(input("Insira um número de 1 a 7:"))

if Dia == 1:
  print("Domingo")
elif Dia == 2:
  print("Segunda")
elif Dia == 3:
  print("terça")
elif Dia == 4:
  print("quarta")
elif Dia == 5:
  print("quinta")
elif Dia == 6:
  print("sexta")
elif Dia == 7:
  print("sábado")
else:
  print("Valor inválido")