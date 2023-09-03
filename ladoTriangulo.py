def calcular_area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area

def calcular_perimetro_triangulo(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    return perimetro

def es_triangulo_rectangulo(lado1, lado2, lado3):
    lados = [lado1, lado2, lado3]
    lados.sort()
    return lados[0]**2 + lados[1]**2 == lados[2]**2

lado1 = float(input("Ingresa la longitud del primer lado del triángulo: "))
lado2 = float(input("Ingresa la longitud del segundo lado del triángulo: "))
lado3 = float(input("Ingresa la longitud del tercer lado del triángulo: "))

area_del_triangulo = calcular_area_triangulo(lado1, lado2)


perimetro_del_triangulo = calcular_perimetro_triangulo(lado1, lado2, lado3)


es_rectangulo = es_triangulo_rectangulo(lado1, lado2, lado3)


print(f"El área del triángulo con lados {lado1}, {lado2} y {lado3} es: {area_del_triangulo}")
print(f"El perímetro del triángulo es: {perimetro_del_triangulo}")
if es_rectangulo:
    print("El triángulo es un triángulo rectángulo.")
else:
    print("El triángulo no es un triángulo rectángulo.")