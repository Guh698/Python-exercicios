verify = False
while verify == False:
    s = str(input("Insira seu sexo com M ou F: ")).upper().replace(" ", "")
    if s == "M":
        print("\nSeu sexo é masculino")
        verify = True
    elif s == "F":
        print("\nSeu sexo é feminino")
        verify = True