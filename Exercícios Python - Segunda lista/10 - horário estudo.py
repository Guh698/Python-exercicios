# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

t = str(input("Insira o turno em que estuda,sendo M-matutino ou V-Vespertino ou N- Noturno:"))

t = t.upper()
t = t.replace(" ", "")

if t == "M":
 print("Bom dia!")
elif t == "V":
  print("Boa tarde!")
elif t == "N":
    print("Boa noite!")
else:
  print("Turno inválido")