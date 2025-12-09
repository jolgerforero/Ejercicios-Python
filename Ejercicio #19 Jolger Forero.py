def volumen_prisma(longitud, ancho, altura):
    volumen= longitud * ancho * altura
    return volumen
longitud = float(input("ingrese la longitud del prisma: "))
ancho = float(input("ingrese el ancho del prisma: "))
altura = float(input("ingrese la altura del prisma: "))
resultado = volumen_prisma(longitud, ancho, altura)
print(f"el volumen del prisma es: {resultado}")