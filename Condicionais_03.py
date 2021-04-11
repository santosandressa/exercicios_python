print("FIAP LIVE")
print("Digite a quantidade de votos para cada dia da semana ")

votosSegunda = input("Segunda-feira: ")
votosSegunda = int(votosSegunda)

votosTerca = input("Terça-feira: ")
votosTerca = int(votosTerca)

votosQuarta = input("Quarta-feira: ")
votosQuarta = int(votosQuarta)

votosQuinta = input("Quinta-feira: ")
votosQuinta = int(votosQuinta)

votosSexta = input("Sexta-feira: ")
votosSexta = int(votosSexta)

diaVencedor = votosSegunda
strDiaVencedor = "Segunda-feira"

if votosSegunda > diaVencedor:
    diaVencedor = votosSegunda
    strDiaVencedor

if votosTerca >= diaVencedor:
    diaVencedor = votosTerca
    strDiaVencedor = "Terça-feira"

if votosQuarta > diaVencedor:
    diaVencedor = votosQuarta
    strDiaVencedor = "Quarta-feira"

if votosQuinta > diaVencedor:
    diaVencedor = votosQuinta
    strDiaVencedor = "Quinta-feira"

if votosSexta > diaVencedor:
    diaVencedor = votosSexta
    strDiaVencedor = "Sexta-feira"

print("{} votos. {} foi o dia escolhido para LIVE".format(diaVencedor, strDiaVencedor))
