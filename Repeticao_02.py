print("Escolha sua Assinatura: | B - Basic | S - Silver | G - Gold | P - Platinum | ")
nivelAssinatura = input()

faturamentoAnual = input("Informe seu faturamento anual: ")

porcentagemBasic = (float(faturamentoAnual) * 30) / 100
porcentagemSilver = (float(faturamentoAnual) * 20) / 100
porcentagemGold = (float(faturamentoAnual) * 10) / 100
porcentagemPlatinum = (float(faturamentoAnual) * 5) / 100

if nivelAssinatura.upper() == 'B':
    print("Valor do bônus a ser pago: R${0:.2f}".format(porcentagemBasic))
elif nivelAssinatura.upper() == 'S':
    print("Valor do bônus a ser pago: R${0:.2f}".format(porcentagemSilver))
elif nivelAssinatura.upper() == 'G':
    print("Valor do bônus a ser pago: R${0:.2f}".format(porcentagemGold))
elif nivelAssinatura.upper() == 'P':
    print("Valor do bônus a ser pago: R${0:.2f}".format(porcentagemPlatinum))
else:
    print("Informe um valor válido")
