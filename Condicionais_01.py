import math

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / math.pow(altura, 2)

if imc < 16.00:
    print("IMC {0:.2f} - Baixo peso Grau III".format(imc))
elif imc >= 16.00 and imc <= 16.99:
    print("IMC {0:.2f} - Baixo peso Grau II".format(imc))
elif imc >= 17.00 and imc <= 18.49:
    print("IMC {0:.2f} - Baixo peso Grau I".format(imc))
elif imc >= 18.50 and imc <= 24.99:
    print("IMC {0:.2f} - Peso Ideal".format(imc))
elif imc >= 25.00 and imc <= 29.99:
    print("IMC {0:.2f} - Sobrepeso".format(imc))
elif imc >= 30.00 and imc <= 34.99:
    print("IMC {0:.2f} - Obesidade Grau I".format(imc))
elif imc >= 35.00 and imc <= 39.99:
    print("IMC {0:.2f} - Obesidade Grau II".format(imc))
else:
    print("IMC {0:.2f} - Obesidade Grau III".format(imc))