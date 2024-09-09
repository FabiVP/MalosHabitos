# Función para calcular el área de un rectángulo
def f(alto, ancho):
    result = alto * ancho
    return result

# Función para calcular el área de un triángulo
def g(base, altura):
    r = 0.5 * base * altura
    return r

# Función principal
if __name__=="__main__":
    alto= float(input("alto: "))
    ancho = float(input("ancho: "))
    rect_area = f(alto, ancho)
    print(f"{"Área del rectángulo : "} {alto}*{ancho}= {rect_area}")

    base = float(input("base: "))
    altura = float(input("altura: "))
    tri_area = g(base, altura)
    print(f"{"Área del triángulo: : "} {base}*{altura}*{0.5}= {tri_area}")

