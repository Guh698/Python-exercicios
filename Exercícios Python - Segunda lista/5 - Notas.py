# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
""""A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

N1 = int(input("insira sua primeira nota:"))
N2 = int(input("Insira sua segunda nota:"))

M = (N1 + N2) /2

if M == 10:
    print("\nAprovado com Distinção")
elif M >= 7:
    print("\nAprovado")
else:
    print("\nReprovado")