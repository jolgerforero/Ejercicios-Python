def capturar_datos():
    longitud = float(input("Ingrese la longitud del prisma: "))
    ancho = float(input("Ingrese el ancho del prisma: "))
    altura = float(input("Ingrese la altura del prisma: "))
    return longitud, ancho, altura

def calcular_volumen(longitud, ancho, altura):
    volumen = longitud * ancho * altura
    return volumen

def imprimir_resultado(volumen):
    print(f"El volumen del prisma rectangular es: {volumen} unidades cúbicas")

# Programa principal
longitud, ancho, altura = capturar_datos()
volumen = calcular_volumen(longitud, ancho, altura)
imprimir_resultado(volumen)