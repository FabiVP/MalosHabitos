

def multiplicacion(factor1, factor2):
    producto = factor1 * factor2
    return producto

if __name__=="__main__":
    multiplicando = float(input ("multiplicando: "))
    multiplicador = float(input ("multiplicador: "))

    resultado = multiplicacion(multiplicando, multiplicador)
    print(f"{"El resultado es : "} {multiplicando}*{multiplicador}= {resultado}")