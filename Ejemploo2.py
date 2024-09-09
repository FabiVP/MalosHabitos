def calcular(factor1, factor2, factor3):
    operacion = factor1 * factor2 + factor3
    return operacion

if __name__=="__main__":
    operador1 = float(input("Operador 1: "))
    operador2 = float(input("Operador 2: "))
    operador3 = float(input("Operador 3: "))

    resultado = calcular(operador1, operador2, operador3)
    print(f"{"El resultado es : "} {operador1}*{operador2}+{operador3}= {resultado}")

