def capturar_datos():
    longitud_lado=float(input("ingrese valor longitud_lado"))
    return longitud_lado

def procesar(longitud_lado):
    volumen= longitud_lado**3
    return volumen

def mostrar(volumen):
    print("equivale a volumen:", volumen)

longitud_lado= capturar_datos()
volumen= procesar(longitud_lado)
mostrar(volumen)