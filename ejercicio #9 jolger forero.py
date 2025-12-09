def capturar_datos():
    base_mayor = float(input("Ingrese la longitud de la base mayor: "))
    base_menor = float(input("Ingrese la longitud de la base menor: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    return base_mayor, base_menor, altura


def calcular_area(base_mayor, base_menor, altura):
    area = ((base_mayor + base_menor) * altura) / 2
    return area


def imprimir_resultado(area):
    print(f"El área del trapecio es: {area:.2f} unidades cuadradas")

#Codigo principal
base_mayor, base_menor, altura = capturar_datos()
area = calcular_area(base_mayor, base_menor, altura)
imprimir_resultado(area)