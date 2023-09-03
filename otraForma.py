def calcular_area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area


def determinar_tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"

lado1 = float(input("Ingresa la longitud del primer lado del triángulo: "))
lado2 = float(input("Ingresa la longitud del segundo lado del triángulo: "))
lado3 = float(input("Ingresa la longitud del tercer lado del triángulo: "))


tipo_de_triangulo = determinar_tipo_triangulo(lado1, lado2, lado3)

area_del_triangulo = calcular_area_triangulo(lado1, lado2)
print(f"El área del triángulo con lados {lado1}, {lado2} y {lado3} es: {area_del_triangulo}")
print(f"El triángulo es de tipo: {tipo_de_triangulo}")