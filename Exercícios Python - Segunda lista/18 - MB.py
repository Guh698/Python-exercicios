# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

Mb = float(input("Insira o tamanho de seu arquivo para download em MB:"))
Mbps = float(input("Insira velocidade de um link de Internet em Mbps:"))

mbps = Mb /Mbps

if mbps < 60:
    print(f"\nO tempo aproximado para o download do arquivo usando este link em é: {mbps} segundos.")
else:
    print(f"\nO tempo aproximado para o download do arquivo usando este link é:{mbps/60} minutos.")
