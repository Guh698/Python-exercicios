# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

s = str(input("Insira seu sexo com M ou F: "))

s = s.upper()
s = s.replace(" ", "")

if s == "M":
    print("\nSeu sexo é masculino")
elif s == "F":
    print("\nSeu sexo é feminino")
else:
    print("\nSexo inválido")