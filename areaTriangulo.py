def calcular_area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area

base = float(input("Ingresa la longitud de la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

area_del_triangulo = calcular_area_triangulo(base, altura)
print(f"El área del triángulo con base {base} y altura {altura} es: {area_del_triangulo}")






